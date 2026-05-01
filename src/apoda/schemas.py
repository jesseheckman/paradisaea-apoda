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

    ordinal_colors: tuple[str, ...] = ()

    def sequential(self, n: int) -> tuple[str, ...]:
        return sequential(self.primary, n)

    def binary(self) -> tuple[str, str]:
        return (self.secondary, self.primary)

    def ordinal(self, n: int | None = None) -> tuple[str, ...]:
        if n is None:
            return self.ordinal_colors
        return self.ordinal_colors[:n]