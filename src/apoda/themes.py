# src/apoda/themes.py

from .schemas import PlotSchema

DEFAULT = PlotSchema(
    name="default",
    primary="#c44e52",
    secondary="#bebebe",
    neutral="#4a4a4a",
)

MINIMAL = PlotSchema(
    name="minimal",
    primary="#c44e52",
    secondary="#bebebe",
    neutral="#222222",
    grid="#eeeeee",
)