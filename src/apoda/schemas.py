# src/apoda/schemas.py

from dataclasses import dataclass
from .generators import interpolate_hex


@dataclass(frozen=True)
class PlotSchema:
    name: str

    primary: str
    secondary: str
    neutral: str

    background: str = "white"
    grid: str = "#e6e6e6"
    helper: str = "#4a4a4a"
    off: str = "#bebebe"

    ordinal_colors: tuple[str, ...] = ()

    def binary(self, accent: str = "primary") -> tuple[str, str]:
        if accent == "primary":
            return (self.off, self.primary)
        if accent == "secondary":
            return (self.off, self.secondary)
        raise ValueError("accent must be 'primary' or 'secondary'.")

    def sequential(self, n: int, between: tuple[str, str]) -> tuple[str, ...]:
        allowed = {"primary", "secondary", "off", "neutral", "helper", "grid", "background"}

        start_name, end_name = between

        if start_name not in allowed or end_name not in allowed:
            raise ValueError(
                f"between must contain valid colour roles: {sorted(allowed)}"
            )

        start = getattr(self, start_name)
        end = getattr(self, end_name)

        return interpolate_hex(start, end, n)

    def ordinal(self, n: int | None = None) -> tuple[str, ...]:
        if n is None:
            return self.ordinal_colors
        return self.ordinal_colors[:n]