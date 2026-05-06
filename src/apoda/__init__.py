from importlib.metadata import version

from .schemas import PlotSchema, AxisStyle
from .themes import DEFAULT, MINIMAL, HARBOR, BOTANICA
from .style import apply, helper_hline, helper_vline

__all__ = [
    "PlotSchema",
    "AxisStyle",
    "DEFAULT",
    "MINIMAL",
    "HARBOR",
    "BOTANICA",
    "apply",
    "helper_hline",
    "helper_vline",
]

__version__ = version("paradisaea-apoda")


def pkaa() -> str:
    return "Pkaa pkaa!"