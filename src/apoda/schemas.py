# src/apoda/schemas.py

from dataclasses import dataclass

@dataclass(frozen=True)
class PlotSchema:
    name: str
    primary: str
    secondary: str
    neutral: str
    background: str = "white"
    grid: str = "#e6e6e6"