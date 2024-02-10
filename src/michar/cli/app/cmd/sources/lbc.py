import rich_click as click
import michar.api.util as util
import michar.api.crawlers.Krawlerz as krawlers
from michar.api.crawlers.Krawlerz import LbcCityKrawler
from michar.cli.app.cmd.crawler import crawl
import time

log = util.get_logger()


@crawl.group()
def lbc():
    """
    Long Beach City Calendar
    """
    print("...lbc...")


@lbc.command()
def matters(year: int):
    """"""
    krawler: LbcCityKrawler = krawlers.get_crawler(source="lbc")

    # crawl_params: dict = {}
    # results: dict = krawler.crawl()
    print("...matters patrolling....")


@lbc.command()
def events(start_time: str, end_time: str):
    """"""
    krawler: LbcCityKrawler = krawlers.get_crawler(source="lbc")

    # crawl_params: dict = {}
    # results: dict = krawler.crawl()
    print("...events patrolling....")
