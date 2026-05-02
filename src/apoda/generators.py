# src/apoda/generators.py

def interpolate_hex(start: str, end: str, n: int) -> tuple[str, ...]:
    """Generate n colours between two hex colours."""

    if n <= 0:
        raise ValueError("n must be > 0")

    def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
        hex_color = hex_color.lstrip("#")
        return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

    def rgb_to_hex(rgb: tuple[int, int, int]) -> str:
        return "#{:02x}{:02x}{:02x}".format(*rgb)

    start_rgb = hex_to_rgb(start)
    end_rgb = hex_to_rgb(end)

    if n == 1:
        return (start,)

    colors = []
    for i in range(n):
        t = i / (n - 1)
        rgb = tuple(
            round(start_rgb[j] * (1 - t) + end_rgb[j] * t)
            for j in range(3)
        )
        colors.append(rgb_to_hex(rgb))

    return tuple(colors)