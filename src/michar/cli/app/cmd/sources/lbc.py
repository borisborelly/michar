import rich_click as click
import michar.api.util as util
import michar.api.crawlers.Krawlerz as krawlers
from michar.api.crawlers.Krawlerz import LbcCityKrawler
from michar.cli.app.cmd.crawler import crawl

log = util.get_logger()


@crawl.group()
def lbc():
    """
    Long Beach City Calendar
    """
    print("...lbc...")


matter_time_stamp_opt: click.Option = click.option(
    "-t", "--time", type="str", help="YYYY-MM-DD", default=None
)


@lbc.command()
# @matter_time_stamp_opt
def matters():
    """"""
    krawler: LbcCityKrawler = krawlers.get_crawler(source="lbc")

    # crawl_params: dict = {}
    # results: dict = krawler.crawl()
    print("...matters patrolling....")


event_start_time_stamp_opt: click.Option = click.option(
    "-b", "--startTime", type="str", help="YYYY-MM-DD", default=None
)
event_end_time_stamp_opt: click.Option = click.option(
    "-b", "--startTime", type="str", help="YYYY-MM-DD", default=None
)


@lbc.command()
# @event_start_time_stamp_opt
# @event_end_time_stamp_opt
def events():
    """"""
    krawler: LbcCityKrawler = krawlers.get_crawler(source="lbc")

    # crawl_params: dict = {}
    # results: dict = krawler.crawl()
    print("...events patrolling....")
