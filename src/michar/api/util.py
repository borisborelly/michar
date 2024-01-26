import logging
from typing import Optional
from rich.logging import RichHandler
import michar.api.crawlers as CRAWL_API

# from michar.api.crawlers.Krawlerz import Krawl, SeleniumKrawler

logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)


def get_logger(name: Optional[str] = "util") -> logging.Logger:
    return logging.getLogger(name)


log = get_logger()
