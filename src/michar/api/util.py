import logging
import rich_click as click
from typing import Optional
from rich.logging import RichHandler
from rich.traceback import install
from rich.console import Console
from rich.theme import Theme
console = Console(theme=Theme({"logging.level.info": "cyan"}))
install()

logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True, tracebacks_suppress=[click])],
)


def get_logger(name: Optional[str] = "util") -> logging.Logger:
    return logging.getLogger(name)