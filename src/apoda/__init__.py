from importlib.metadata import version

from .schemas import PlotSchema
from .themes import DEFAULT, MINIMAL, HARBOR
from .style import apply, helper_hline, helper_vline

__all__ = [
    "PlotSchema",
    "DEFAULT",
    "MINIMAL",
    "HARBOR",
    "apply",
    "helper_hline",
    "helper_vline",
]

__version__ = version("paradisaea-apoda")


def pkaa() -> str:
    return "Pkaa pkaa!"