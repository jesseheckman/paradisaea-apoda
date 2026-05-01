# src/apoda/style.py

from cycler import cycler
import matplotlib.pyplot as plt


_ACTIVE_SCHEMA = None

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

    global _ACTIVE_SCHEMA
    _ACTIVE_SCHEMA = schema

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

def _resolve_schema(schema):
    if schema is not None:
        return schema
    if _ACTIVE_SCHEMA is None:
        raise ValueError("No active schema. Call ap.apply() first.")
    return _ACTIVE_SCHEMA

def helper_hline(ax, y: float, schema=None, **kwargs):
    schema = _resolve_schema(schema)

    defaults = {
        "color": schema.helper,
        "linestyle": "--",
        "linewidth": 1.0,
        "alpha": 0.8,
    }
    defaults.update(kwargs)

    return ax.axhline(y, **defaults)


def helper_vline(ax, x: float, schema=None, **kwargs):
    schema = _resolve_schema(schema)

    defaults = {
        "color": schema.helper,
        "linestyle": "--",
        "linewidth": 1.0,
        "alpha": 0.8,
    }
    defaults.update(kwargs)

    return ax.axvline(x, **defaults)