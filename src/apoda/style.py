# src/apoda/style.py

from cycler import cycler
import matplotlib as mpl
import matplotlib.pyplot as plt

from .schemas import AxisStyle, merge_axis


_ACTIVE_SCHEMA = None


def cmap(schema=None, *, low=None, high=None, name=None):
    """
    Create a Matplotlib colormap from an apoda schema.
    """

    schema = schema or _ACTIVE_SCHEMA

    if schema is None:
        raise ValueError(
            "No schema provided and no active schema set. "
            "Call style.apply(schema) first or pass schema explicitly."
        )

    low = low or schema.secondary
    high = high or schema.primary

    return mpl.colors.LinearSegmentedColormap.from_list(
        name or f"apoda_{schema.name}",
        [low, high],
    )

def get_palette(
    schema,
    palette: str = "binary",
    n: int | None = None,
    accent: str = "primary",
    between: tuple[str, str] | None = None,
) -> tuple[str, ...]:

    if palette == "binary":
        return schema.binary(accent=accent)

    if palette == "sequential":
        if n is None:
            raise ValueError("n must be provided for sequential palettes.")

        if between is None:
            between = ("off", "primary")

        return schema.sequential(n=n, between=between)

    if palette == "ordinal":
        return schema.ordinal(n)

    raise ValueError(f"Unknown palette: {palette}")


def apply(
    schema,
    palette: str = "binary",
    n: int | None = None,
    accent: str = "primary",
    between: tuple[str, str] | None = None,
    axis: AxisStyle | dict | None = None,
) -> None:
    """Apply an Apoda plot schema to Matplotlib."""

    global _ACTIVE_SCHEMA
    _ACTIVE_SCHEMA = schema

    if isinstance(axis, dict):
        axis = AxisStyle(**axis)

    axis_style = merge_axis(
        getattr(schema, "axis", None),
        axis,
    )

    colors = get_palette(
        schema,
        palette=palette,
        n=n,
        accent=accent,
        between=between,
    )

    plt.rcParams.update({

        # Colour cycle
        "axes.prop_cycle": cycler(color=colors),

        # Figure
        "figure.figsize": (10, 4),
        "figure.dpi": 100,

        # Backgrounds
        "figure.facecolor": schema.fig_background,
        "axes.facecolor": schema.background,
        "savefig.facecolor": schema.fig_background,

        # Grid
        "axes.grid": True,
        "axes.axisbelow": True,
        "grid.color": schema.grid,
        "grid.linestyle": "-",
        "grid.linewidth": 1,
        "grid.alpha": 0.2,

        # Spines
        "axes.spines.top": axis_style.top,
        "axes.spines.right": axis_style.right,
        "axes.spines.left": axis_style.left,
        "axes.spines.bottom": axis_style.bottom,

        "axes.linewidth": axis_style.linewidth,
        "axes.edgecolor": axis_style.edgecolor or schema.neutral,

        # Tick placement
        "xtick.top": axis_style.xtick_top,
        "ytick.right": axis_style.ytick_right,

        # Tick direction
        "xtick.direction": axis_style.tick_direction,
        "ytick.direction": axis_style.tick_direction,

        # Text colours
        "text.color": schema.neutral,
        "axes.labelcolor": schema.neutral,
        "xtick.color": schema.neutral,
        "ytick.color": schema.neutral,

        # Legend
        "legend.edgecolor": schema.grid,
        "legend.facecolor": schema.background,
        "legend.framealpha": 1.0,
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

    line = ax.axhline(y, **defaults)
    line._apoda_helper = True

    return line


def helper_vline(ax, x: float, schema=None, **kwargs):

    schema = _resolve_schema(schema)

    defaults = {
        "color": schema.helper,
        "linestyle": "--",
        "linewidth": 1.0,
        "alpha": 0.8,
    }

    defaults.update(kwargs)

    line = ax.axvline(x, **defaults)
    line._apoda_helper = True   

    return line