import rich_click as click
import michar.api.util as util
from typing import List
from michar.cli.app.michar import gooza



url_option : click.Option = click.option("-U", "--url", required=False, default="https://longbeach.legistar.com/calendar.aspx", type=str, help="website to crawl for data")

@gooza.command()
@url_option
def crawl(url: str):
    """
    crawl websites for data
    """
    log = util.get_logger()
    krawler: util.Krawl = util.get_crawler(url=url)


    content_div = krawler.get_div('ctl00_ContentPlaceHolder1_divGrid')
    log.info(content_div)


    krawler.shutdown()
    