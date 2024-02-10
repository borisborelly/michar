import rich_click as click
import michar.api.util as util
import michar.api.crawlers.Krawlerz as krawlers
from michar.cli.app.cmd.crawler import crawl

log = util.get_logger()


@crawl.group()
def torrance():
    # https://www.torranceca.gov/government/city-clerk/commissions-and-advisory-boards/planning-commission/agendas-and-minutes/-folder-1334
    print("TODO research torrance")

    krawler: krawlers.LbcCityKrawler = krawlers.get_crawler(source="torrance")
