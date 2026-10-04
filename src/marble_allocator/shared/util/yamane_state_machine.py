from typing import Any, Callable, Optional

from dataclasses import dataclass

@dataclass(frozen=True)
class StateContext:
    current_raw_time: float   # アプリの絶対時間(getFrameTime)
    dt: float                 # このフレームで進めるべき時間（引き算で計算）
    state_time: float         # このステートが始まってからの経過秒数（引き算で計算）
    is_first: bool            # ステート切り替わり直後のフレームか


class StateMachine:
    def __init__(self, owner: Any):
        self.__owner = owner
        self.__current_state: Optional[Callable[[StateContext], None]] = None
        self.__next_state: Optional[Callable[[StateContext], None]] = None

        self.__state_start_time = 0.0  # ステートが始まった時の「アプリ絶対時間」
        self.__overflow_time = 0.0     # 遷移時に持ち越されたあふれ時間

    def update(self, current_raw_time: float, frame_dt: float):
        """
        現在のアプリ絶対時間(getFrameTime()) と、最上位で計算された frame_dt を受け取ります。
        """
        # 1. 通常実行（遷移要求がない場合）
        if self.__current_state and not self.__next_state:
            # ★ 加算ではなく、引き算でステート経過時間を計算（累積誤差ゼロ）
            state_time = current_raw_time - self.__state_start_time
            ctx = StateContext(current_raw_time=current_raw_time, dt=frame_dt, state_time=state_time, is_first=False)
            self.__current_state(ctx)

        # 2. 即時遷移の実行
        while self.__next_state:
            current_overflow = self.__overflow_time
            self.__overflow_time = 0.0  # リセット
            
            self.__current_state = self.__next_state
            self.__next_state = None
            
            # あふれた分（過去）に遡って、新しいステートの開始時間を設定
            self.__state_start_time = current_raw_time - current_overflow
            
            ctx = StateContext(
                current_raw_time=current_raw_time,
                # overflowを使わないなら通常のdt、使うならあふれ時間（0.006秒など）だけにする
                dt=current_overflow if current_overflow > 0.0 else frame_dt,
                state_time=current_overflow,
                is_first=True
            )
            self.__current_state(ctx)

    def set_next_state(self, state: Callable[[StateContext], None], overflow_time: float = 0.0):
        self.__next_state = state
        self.__overflow_time = overflow_time
