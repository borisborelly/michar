import rich_click as click
import michar.api.util as util
from michar.cli.app.michar import gooza

report_type_opt: click.Option = click.option(
    "-o",
    "--reportType",
    required=False,
    default="csv",
    type=str,
    help="what kind of report to generate",
)


@gooza.command()
@report_type_opt
def report(reporttype: str):
    """
    generate report from results of crawling
    """
    log = util.get_logger()
    log.info(f"reporting {reporttype}")
