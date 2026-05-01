# src/apoda/style.py

from cycler import cycler
import matplotlib.pyplot as plt


def get_palette(schema, palette: str = "binary", n: int | None = None) -> tuple[str, ...]:
    if palette == "binary":
        return schema.binary()

    if palette == "sequential":
        if n is None:
            raise ValueError("n must be provided for sequential palettes.")
        return schema.sequential(n)

    if palette == "ordinal":
        return schema.ordinal(n)

    raise ValueError(f"Unknown palette: {palette}")


def apply(schema, palette: str = "binary", n: int | None = None) -> None:
    """Apply an Apoda plot schema to Matplotlib."""

    colors = get_palette(schema, palette=palette, n=n)

    plt.rcParams.update({
        "axes.prop_cycle": cycler(color=colors),
        "figure.figsize": (10, 4),
        "figure.dpi": 100,
        "axes.grid": True,
        "axes.axisbelow": True,
        "grid.color": schema.grid,
        "grid.linestyle": "--",
        "grid.linewidth": 0.8,
        "grid.alpha": 0.6,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "text.color": schema.neutral,
        "axes.labelcolor": schema.neutral,
        "xtick.color": schema.neutral,
        "ytick.color": schema.neutral,
    })


def helper_hline(ax, y: float, schema, **kwargs):
    """Draw a horizontal helper/reference line."""

    defaults = {
        "color": schema.helper,
        "linestyle": "--",
        "linewidth": 1.0,
        "alpha": 0.8,
    }
    defaults.update(kwargs)

    return ax.axhline(y, **defaults)


def helper_vline(ax, x: float, schema, **kwargs):
    """Draw a vertical helper/reference line."""

    defaults = {
        "color": schema.helper,
        "linestyle": "--",
        "linewidth": 1.0,
        "alpha": 0.8,
    }
    defaults.update(kwargs)

    return ax.axvline(x, **defaults)