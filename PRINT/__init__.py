import sys
import types

from .PRINT import ascii_color_print


class ItHASToBeAClass(types.ModuleType):
    def __call__(self, value: str) -> None:
        ascii_color_print(value)


sys.modules[__name__].__class__ = ItHASToBeAClass
