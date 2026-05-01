from importlib.metadata import version
from .schemas import PlotSchema
from .themes import DEFAULT, MINIMAL

__all__ = ["PlotSchema", "DEFAULT", "MINIMAL"]
__version__ = version("paradisaea-apoda")

def pkaa() -> str:
    return "Pkaa pkaa!"

