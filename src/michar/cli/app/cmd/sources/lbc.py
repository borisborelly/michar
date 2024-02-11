import rich_click as click
import michar.api.util as util
import michar.api.crawlers.Krawlerz as krawlers
from michar.api.crawlers.Krawlerz import LBC
from michar.cli.app.cmd.crawler import crawl
from michar.api.sources.legistar import Event, Matter
from rich.console import Console
from rich.markdown import Markdown

log = util.get_logger()


@crawl.group()
def lbc():
    """
    Long Beach City Calendar
    """
    print("...lbc...")


@lbc.command()
# @click.option("-t", "--time", type="str", help="YYYY-MM-DD", default=None)
def matters():
    """
    Search for LBC Matters
    """
    krawler: LBC = krawlers.get_crawler(source="lbc")
    matters: list[Matter] = krawler.matters

    headers = list(matters[0].dict.keys())
    data = [obj.dict for obj in matters]
    from tabulate import tabulate

    markdown_table = tabulate(matters, headers=headers, tablefmt="pipe")

    # Print Markdown table
    print(markdown_table)

    # crawl_params: dict = {}
    # results: dict = krawler.crawl()
    # console = Console()
    # for m in matters:
    #     md = Markdown(m.markdown)
    #     # print(e.markdown)
    #     console.print(md)
    print("...matters patrolling....")


event_start_time_stamp_opt: click.Option = click.option(
    "-b", "--startTime", type="str", help="YYYY-MM-DD", default=None
)
event_end_time_stamp_opt: click.Option = click.option(
    "-e", "--endTime", type="str", help="YYYY-MM-DD", default=None
)


@lbc.command()
# @event_start_time_stamp_opt
# @event_end_time_stamp_opt
def events():
    """
    Search for LBC Events
    """
    krawler: LBC = krawlers.get_crawler(source="lbc")
    events: list[Event] = krawler.events

    headers = list(events[0].dict.keys())
    print(f"{headers=}")
    data = [obj.dict for obj in events]
    from tabulate import tabulate

    markdown_table = tabulate(events, headers=headers, tablefmt="pipe")

    # Print Markdown table
    print(markdown_table)

    # for e in events:
    #     md = Markdown(e.markdown)
    #     # print(e.markdown)
    #     console.print(md)

    # filename = "report.md"
    # with open(filename, "w") as file:
    #     for e in events:
    #         file.write(e.markdown)
    #         print(e.markdown)
    # log.info(f"Results: {filename}")

    # crawl_params: dict = {}
    # results: dict = krawler.crawl()
    print("...events patrolling....")
