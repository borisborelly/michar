"""_summary_ example app"""
import rich_click as click
import michar.api.util as util
import logging
from michar import __version__, __name__
from trogon import tui


debug_option: click.Option = click.option(
    "-d", "--debug", default=False, is_flag=True, help="debug logs"
)

log: logging.Logger = util.get_logger()


class MichiOptions(object):
    def __init__(self, *args, **kwargs):
        [self.__setattr__(kk, vv) for kk, vv in kwargs.items()]


@tui(help="Open terminal UI")
@click.group(context_settings=dict(help_option_names=["-h", "--help"]), chain=True)
@debug_option
@click.version_option(__version__, prog_name=__name__)
@click.pass_context
def gooza(ctx: click.Context, debug) -> None:
    if debug:
        for logger in [
            logging.getLogger(name) for name in logging.root.manager.loggerDict
        ]:
            logger.setLevel(logging.DEBUG)
    log.debug(f"Starting michar library ... {__version__}")


# TODO fix * import
from .cmd.crawler import *
from .cmd.reporter import *


def main():
    """
    :meta: private
    """
    gooza(obj=MichiOptions(help=None, debug=None))
