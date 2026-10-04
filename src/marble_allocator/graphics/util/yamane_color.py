import colorsys

class ColorConverter:
    # ------------------------------------------------------------
    # Gamma conversion
    # ------------------------------------------------------------
    @staticmethod
    def srgb_to_linear(c: float) -> float:
        if c <= 0.04045:
            return c / 12.92
        return ((c + 0.055) / 1.055) ** 2.4

    @staticmethod
    def linear_to_srgb(c: float) -> float:
        if c <= 0.0031308:
            return 12.92 * c
        return 1.055 * (c ** (1/2.4)) - 0.055

    @staticmethod
    def rgb_float_to_linear(rgb: tuple[float, float, float]):
        r, g, b = rgb
        return (
            ColorConverter.srgb_to_linear(r),
            ColorConverter.srgb_to_linear(g),
            ColorConverter.srgb_to_linear(b)
        )

    @staticmethod
    def rgb_float_to_srgb(rgb: tuple[float, float, float]):
        r, g, b = rgb
        return (
            ColorConverter.linear_to_srgb(r),
            ColorConverter.linear_to_srgb(g),
            ColorConverter.linear_to_srgb(b)
        )

    @staticmethod
    def rgb_float_to_byte(rgb: tuple[float, float, float]):
        r, g, b = rgb
        return (round(r * 255), round(g * 255), round(b * 255))

    @staticmethod
    def rgb_float_to_hex(rgb: tuple[float, float, float]):
        r, g, b = rgb
        return "#%02x%02x%02x" % (
            int(r * 255),
            int(g * 255),
            int(b * 255),
        )

    # ------------------------------------------------------------
    # HSV(deg) → RGB
    # ------------------------------------------------------------
    @staticmethod
    def hsv_deg_linear_to_rgb_linear(hsv: tuple[int, int, int]):
        h = hsv[0] / 360
        s = hsv[1] / 100
        v = hsv[2] / 100
        return colorsys.hsv_to_rgb(h, s, v)

    @staticmethod
    def hsv_deg_linear_to_rgb_srgb(hsv: tuple[int, int, int]):
        rgb_lin = ColorConverter.hsv_deg_linear_to_rgb_linear(hsv)
        return ColorConverter.rgb_float_to_srgb(rgb_lin)

    @staticmethod
    def hsv_deg_srgb_to_rgb_linear(hsv: tuple[int, int, int]):
        h = hsv[0] / 360
        s_srgb = hsv[1] / 100
        v_srgb = hsv[2] / 100
        rgb_s = colorsys.hsv_to_rgb(h, s_srgb, v_srgb)
        return ColorConverter.rgb_float_to_linear(rgb_s)

    @staticmethod
    def hsv_deg_srgb_to_rgb_srgb(hsv: tuple[int, int, int]):
        h = hsv[0] / 360
        s_srgb = hsv[1] / 100
        v_srgb = hsv[2] / 100
        return colorsys.hsv_to_rgb(h, s_srgb, v_srgb)

    # ------------------------------------------------------------
    # HSV(unit) → RGB
    # ------------------------------------------------------------
    @staticmethod
    def hsv_unit_linear_to_rgb_linear(hsv: tuple[float, float, float]):
        return colorsys.hsv_to_rgb(hsv[0], hsv[1], hsv[2])

    @staticmethod
    def hsv_unit_linear_to_rgb_srgb(hsv: tuple[float, float, float]):
        rgb_lin = ColorConverter.hsv_unit_linear_to_rgb_linear(hsv)
        return ColorConverter.rgb_float_to_srgb(rgb_lin)

    @staticmethod
    def hsv_unit_srgb_to_rgb_linear(hsv: tuple[float, float, float]):
        rgb_s = colorsys.hsv_to_rgb(hsv[0], hsv[1], hsv[2])
        return ColorConverter.rgb_float_to_linear(rgb_s)

    @staticmethod
    def hsv_unit_srgb_to_rgb_srgb(hsv: tuple[float, float, float]):
        return colorsys.hsv_to_rgb(hsv[0], hsv[1], hsv[2])

    # ------------------------------------------------------------
    # RGB → RGB (gamma conversion)
    # ------------------------------------------------------------
    @staticmethod
    def rgb_byte_to_linear(rgb: tuple[int, int, int]):
        r = rgb[0] / 255
        g = rgb[1] / 255
        b = rgb[2] / 255
        return ColorConverter.rgb_float_to_linear((r, g, b))

    @staticmethod
    def rgb_byte_to_srgb(rgb: tuple[int, int, int]):
        return (rgb[0] / 255, rgb[1] / 255, rgb[2] / 255)

    @staticmethod
    def rgb_float_to_linear_rgb(rgb: tuple[float, float, float]):
        return ColorConverter.rgb_float_to_linear(rgb)

    @staticmethod
    def rgb_float_to_srgb_rgb(rgb: tuple[float, float, float]):
        return ColorConverter.rgb_float_to_srgb(rgb)

    # ------------------------------------------------------------
    # Luminance
    # ------------------------------------------------------------
    @staticmethod
    def luminance_linear(rgb: tuple[float, float, float]) -> float:
        r, g, b = rgb
        return 0.2126 * r + 0.7152 * g + 0.0722 * b

    @staticmethod
    def luminance_srgb(rgb: tuple[float, float, float]) -> float:
        r_lin, g_lin, b_lin = ColorConverter.rgb_float_to_linear(rgb)
        return ColorConverter.luminance_linear((r_lin, g_lin, b_lin))
