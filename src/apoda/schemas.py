# src/apoda/schemas.py

from dataclasses import dataclass
from .generators import interpolate_hex


@dataclass(frozen=True)
class AxisStyle:
    top: bool | None = None
    right: bool | None = None
    bottom: bool | None = None
    left: bool | None = None

    linewidth: float | None = None
    edgecolor: str | None = None

    xtick_top: bool | None = None
    ytick_right: bool | None = None
    tick_direction: str | None = None

DEFAULT_AXIS = AxisStyle(
    top=False,
    right=False,
    bottom=True,
    left=True,
    linewidth=1.0,
    edgecolor=None,
    xtick_top=False,
    ytick_right=False,
    tick_direction="out",
)

def merge_axis(*styles: AxisStyle | None) -> AxisStyle:
    values = DEFAULT_AXIS.__dict__.copy()

    for style in styles:
        if style is None:
            continue

        for key, value in style.__dict__.items():
            if value is not None:
                values[key] = value

    return AxisStyle(**values)


@dataclass(frozen=True)
class PlotSchema:
    name: str

    primary: str
    secondary: str 
    neutral: str    # Lines, text, etc.

    fig_background: str = "white"
    background: str = "white"
    grid: str = "#e6e6e6"
    helper: str = "#4a4a4a"
    off: str = "#bebebe"
    ordinal_colors: tuple[str, ...] = ()

    axis: AxisStyle | None = None
    

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
    

class default_spines(tuple[bool, bool, bool, bool]):
    def __new__(cls):
        return super().__new__(cls, (False, False, False, False))