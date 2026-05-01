# src/apoda/generators.py

import colorsys


def sequential(hex_color: str, n: int) -> tuple[str, ...]:
    """Generate n perceptually reasonable sequential shades from a base colour."""

    if n <= 0:
        raise ValueError("n must be > 0")

    hex_color = hex_color.lstrip("#")
    r, g, b = tuple(int(hex_color[i:i+2], 16) / 255 for i in (0, 2, 4))
    h, l, s = colorsys.rgb_to_hls(r, g, b)

    min_l = max(0.15, l * 0.6)
    max_l = min(0.9, l * 1.3)

    shades = []
    for i in range(n):
        t = i / (n - 1) if n > 1 else 0.5  # voorkomt divide-by-zero
        new_l = min_l + (max_l - min_l) * t

        r2, g2, b2 = colorsys.hls_to_rgb(h, new_l, s)

        shades.append("#{:02x}{:02x}{:02x}".format(
            int(r2 * 255),
            int(g2 * 255),
            int(b2 * 255),
        ))

    return tuple(shades)