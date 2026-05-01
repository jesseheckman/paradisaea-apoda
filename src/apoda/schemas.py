# src/apoda/schemas.py

from dataclasses import dataclass
from .generators import sequential

@dataclass(frozen=True)
class PlotSchema:
    name: str
    primary: str
    secondary: str
    neutral: str
    background: str = "white"
    grid: str = "#e6e6e6"
    helper: str = "#4a4a4a"

    def sequential(self, n: int):
        return sequential(self.primary, n)




