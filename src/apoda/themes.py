# src/apoda/themes.py

from .schemas import PlotSchema

DEFAULT = PlotSchema(
    name="default",
    primary="#bebebe",
    secondary="#c44e52",
    neutral="#4a4a4a",
)

MINIMAL = PlotSchema(
    name="minimal",
    primary="#bebebe",
    secondary="#c44e52",
    neutral="#222222",
    grid="#eeeeee",
)