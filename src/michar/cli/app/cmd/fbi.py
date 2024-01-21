import json
import os
import pathlib
import time
from datetime import timedelta

import click
import platformdirs
import structlog

from  michar.cli.app.michar import gooza
from michar.api.fbi.client import FBIClient


log = structlog.get_logger()

@gooza.group()
@click.pass_context
def fbi(ctx: click.Context):
    """
    FBI, open up!
    
    Subcommands will interact with data from the
    [FBI Crime Data API](https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/docApi)

    To authenticate, set an environment variable named FBI_API_KEY.
    You can request an API_KEY here https://api.data.gov/signup/
    """
    ctx.obj = FBIClient()

@fbi.command
@click.pass_obj
def init(client: FBIClient):
    '''Will create an application cache of key identifiers. Run before other subcommands.'''
    dir = platformdirs.user_cache_dir("michar", "Michar Industries Ltd.")
    os.makedirs(dir, exist_ok=True)
    ori_file = pathlib.Path(dir) / "ori_cache.json"
    with ori_file.open('w') as fout:
        log.info("writing to ORI cache", path=ori_file.absolute)
        start = time.perf_counter_ns()
        oris = client.get_all_agency_oris()
        fout.write('[')
        first = True
        for ori in oris:
            if first:
                first = False
            else:
                fout.write(",")
            fout.write(f'"{ori}"')
        fout.write(']')

        end = time.perf_counter_ns()
        log.info("finished caching ORIs", elapsed_seconds=(end-start) / 10**9 )
        