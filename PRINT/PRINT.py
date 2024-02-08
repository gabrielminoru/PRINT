import random
from typing import Any

import colorama
from colorama import Fore
from pyfiglet import Figlet

colorama.init()

COLORS = [
    Fore.RED,
    Fore.GREEN,
    Fore.YELLOW,
    Fore.BLUE,
    Fore.MAGENTA,
    Fore.CYAN,
    Fore.WHITE,
]


def ascii_color_print(value: Any, font: str = "larry3d") -> None:
    txt = str(value)
    ascii_text = Figlet(font=font).renderText(txt)
    colored_text = "".join([random.choice(COLORS) + l for l in ascii_text])
    print(colored_text)
