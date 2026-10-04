from pathlib import Path
import re

class PathManager:
    PROJECT_ROOT = Path(__file__).resolve().parents[4]

    RESOURCE_DIR = PROJECT_ROOT / "resources"

    @staticmethod
    def to_vfs(path: Path) -> str:
        """
        Windows の絶対パスを Panda3D VFS 形式に変換する
        例: D:/path/to/file → /d/path/to/file
        """
        posix = path.as_posix()

        # Windows ドライブレターを検出
        match = re.match(r"([A-Za-z]):/(.*)", posix)
        if match:
            drive = match.group(1).lower()
            rest = match.group(2)
            return f"/{drive}/{rest}"

        return posix  # もともと UNIX 形式ならそのまま

    @classmethod
    def resource(cls, *paths: str):
        p = cls.RESOURCE_DIR.joinpath(*paths)
        return p
    
    @classmethod
    def resource_vfs(cls, *paths: str):
        p = cls.RESOURCE_DIR.joinpath(*paths)
        return cls.to_vfs(p)


#print(PathManager.PROJECT_ROOT)