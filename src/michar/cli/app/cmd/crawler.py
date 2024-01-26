import rich_click as click
import michar.api.util as util
import michar.api.crawlers.Krawlerz as krawlers
from typing import List
from michar.cli.app.michar import gooza
from michar.api.profile import ConfigProfile


url_option: click.Option = click.option(
    "-U",
    "--url",
    required=False,
    default="https://longbeach.legistar.com/calendar.aspx",
    type=str,
    help="website to crawl for data",
)

source_option: click.Option = click.option(
    "-s",
    "--source",
    required=True,
    default="lbc",
    type=click.Choice(["lbc", "fbi"], case_sensitive=False),
)


@gooza.command()
@source_option
def crawl(source: str):
    """
    crawl websites for data
    """
    log = util.get_logger()
    profile: ConfigProfile = ConfigProfile()

    url: str = profile.get_source_url(source)
    krawler: krawlers.Krawl = krawlers.get_crawler(url=url)

    # content_div = krawler.get_div("ctl00_ContentPlaceHolder1_divGrid")
    # log.info(content_div)

    krawler.shutdown()
