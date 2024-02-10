from michar.cli.app.michar import gooza


@gooza.group()
def crawl() -> None:
    """
    crawl for data from available sources
    """
    pass


from .sources.lbc import *
from .sources.torrance import *
