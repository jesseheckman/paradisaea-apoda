# src/apoda/generators.py

import colorsys


def sequential(hex_color: str, n: int):
    """Generate n sequential shades from a base colour."""
    
    hex_color = hex_color.lstrip("#")
    r, g, b = tuple(int(hex_color[i:i+2], 16)/255 for i in (0, 2, 4))

    h, l, s = colorsys.rgb_to_hls(r, g, b)

    # varieer lightness
    shades = []
    for i in range(n):
        # van licht -> donker
        new_l = min(1, max(0, l * (0.5 + i / (n * 0.8))))
        r2, g2, b2 = colorsys.hls_to_rgb(h, new_l, s)

        shades.append("#{:02x}{:02x}{:02x}".format(
            int(r2 * 255),
            int(g2 * 255),
            int(b2 * 255),
        ))

    return shades