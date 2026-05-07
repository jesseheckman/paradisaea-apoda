# src/apoda/themes.py

from .schemas import AxisStyle, PlotSchema

DEFAULT = PlotSchema(
    name="default", 
    primary="#c44e52",
    secondary="#4c72b0",
    neutral="#4a4a4a",
    helper="#aaaaaa",
    grid="#e6e6e6",
    ordinal_colors=(
        "#c44e52",
        "#4c72b0",
        "#55a868",
        "#dd8452",
        "#8172b3",
    ),
)

MINIMAL = PlotSchema(
    name="minimal",
    primary="#bebebe",
    secondary="#c44e52",
    neutral="#222222",
    helper="#888888",
    grid="#eeeeee",
    ordinal_colors=(
        "#c44e52",
        "#999999",
        "#bbbbbb",
    ),
)

HARBOR = PlotSchema(
    name="harbor", 
    primary="#63a89c",
    secondary="#9c4f34",
    neutral="#182D37",
    helper="#5f3b2e",
    grid="#e6e6e6",
    ordinal_colors=(
        "#63a89c",
        "#3f5d7a",
        "#9c4f34",
        "#1e2224",
        "#e6e6e6",
    ),
)

BOTANICA = PlotSchema(
    name="botanica", 
    primary="#297E70",
    secondary="#AA2B4B",
    background="#F9EED7",
    fig_background="#FDFAF2",
    neutral="#4D3F25",
    helper="#5f3b2e",
    grid="#7C6F55",
    ordinal_colors=(
        "#297E70",
        "#48AB9B",
        "#AA2B4B",
        "#BB6379FF",
        "#264887",
        "#5D7CB5",
    ),
    axis=AxisStyle(
        top=True,
        right=True,
        linewidth=0.8,
    ),
)
