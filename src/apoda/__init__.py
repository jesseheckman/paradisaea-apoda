from importlib.metadata import version

from .schemas import PlotSchema
from .themes import DEFAULT, MINIMAL
from .style import apply, helper_hline, helper_vline

__all__ = [
    "PlotSchema",
    "DEFAULT",
    "MINIMAL",
    "JUNANA",
    "apply",
    "helper_hline",
    "helper_vline",
]

__version__ = version("paradisaea-apoda")


def pkaa() -> str:
    return "Pkaa pkaa!"