# src/apoda/effects.py

def sparkle(
    ax=None,
    line=None,
    n=800,
    jitter=0.018,
    size_mean=6,
    size_scale=0.9,
    size_max=42,
    alpha=0.75,
    color="white",
    seed=None,
):
    """
    Add atmospheric sparkle particles around a plotted line.

    Parameters
    ----------
    color :
        - Single matplotlib colour
        - List/tuple of colours
        - If multiple colours are provided,
          particles are randomly assigned.
    """

    import numpy as np
    import matplotlib.pyplot as plt

    rng = np.random.default_rng(seed)

    if ax is None:
        ax = plt.gca()

    # Automatically select last non-helper line
    if line is None:

        candidate_lines = [
            l for l in ax.lines
            if not getattr(l, "_apoda_helper", False)
        ]

        if not candidate_lines:
            raise ValueError("No non-helper lines found on the axes.")

        line = candidate_lines[-1]

    x = np.asarray(line.get_xdata(), dtype=float)
    y = np.asarray(line.get_ydata(), dtype=float)

    mask = np.isfinite(x) & np.isfinite(y)

    x = x[mask]
    y = y[mask]

    if len(x) < 2:
        raise ValueError("Line needs at least two finite points.")

    # Ensure sorted interpolation
    order = np.argsort(x)

    x = x[order]
    y = y[order]

    x_min = np.nanmin(x)
    x_max = np.nanmax(x)

    # Sample random positions along line
    xs = rng.uniform(x_min, x_max, size=n)

    # Interpolate true line position
    y_line = np.interp(xs, x, y)

    x_span = x_max - x_min
    y_span = np.nanmax(y) - np.nanmin(y)

    # Organic particle cloud around line
    xs = xs + rng.normal(
        0,
        jitter * x_span,
        size=n,
    )

    ys = y_line + rng.normal(
        0,
        jitter * y_span,
        size=n,
    )

    # Mostly tiny particles + rare large sparkles
    sizes = rng.lognormal(
        mean=np.log(size_mean),
        sigma=size_scale,
        size=n,
    )

    sizes = np.clip(
        sizes,
        1,
        size_max,
    )

    # MULTI-COLOUR SUPPORT
    if isinstance(color, (list, tuple, np.ndarray)):
        colors = rng.choice(color, size=n)
    else:
        colors = color

    return ax.scatter(
        xs,
        ys,
        s=sizes,
        c=colors,
        alpha=alpha,
        linewidths=0,
        zorder=-999,
    )