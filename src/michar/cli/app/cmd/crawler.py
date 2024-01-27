import rich_click as click
import michar.api.util as util
import michar.api.crawlers.Krawlerz as krawlers
from typing import List
from michar.cli.app.michar import gooza
from michar.api.profile import ConfigProfile


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

    krawler: krawlers.Krawl = krawlers.get_crawler(source=source)

    # torrence
    # https://www.torranceca.gov/government/city-clerk/commissions-and-advisory-boards/planning-commission/agendas-and-minutes/-folder-1334
