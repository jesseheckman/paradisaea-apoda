# src/apoda/themes.py

from .schemas import PlotSchema

DEFAULT = PlotSchema(
    name="default", 
    primary="#c44e52",
    secondary="#4c72b0",
    neutral="#222222",
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