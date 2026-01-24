# src/printrgb/printrgb.pyi
from typing import Literal, Callable, Any, TextIO

def get_color_default(angle: int) -> tuple[int, int, int]: ...

class printrgb:
    def __call__(
        self,
        *values: object,
        foreground_color: list[int] | tuple[int, int, int] | None = None,
        background_color: list[int] | tuple[int, int, int] | None = None,
        sep: str = " ",
        rainbow: bool = False,
        angle_mode: Literal['inner', 'init', 'random'] = 'random',
        end: str = "\n",
        file: TextIO | Any | None = None,
        get_color: Callable[[int], tuple[int, int, int]] | None = None,
        flush: Literal[False] = False,
        swap_fbc: bool = False,
        allow_rainbow_blank: bool = False,
    ) -> None: ...


