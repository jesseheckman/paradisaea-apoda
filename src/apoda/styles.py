# src/apoda/style.py

from cycler import cycler
import matplotlib.pyplot as plt


def apply(schema) -> None:
    """Apply an Apoda plot schema to Matplotlib."""

    plt.rcParams.update({
        # Data colour cycle
        "axes.prop_cycle": cycler(color=[
            schema.primary,
            schema.secondary,
        ]),

        # Figure / axes
        "figure.figsize": (10, 4),
        "figure.dpi": 100,
        "axes.grid": True,
        "axes.axisbelow": True,

        # Grid
        "grid.color": schema.grid,
        "grid.linestyle": "--",
        "grid.linewidth": 0.8,
        "grid.alpha": 0.6,

        # Spines
        "axes.spines.top": False,
        "axes.spines.right": False,

        # Text / ticks
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