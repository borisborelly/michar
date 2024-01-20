import click
from  michar.cli.app.michar import gooza
from michar.api.fbi.client import FBIClient

@gooza.group()
@click.pass_context
def fbi(ctx: click.Context):
    """FBI, open up!"""
    ctx.obj = FBIClient()

@fbi.command
@click.pass_obj
def init(client: FBIClient):
    '''Will create an application cache of key identifiers. Run before other subcommands.'''
    oris = client.get_all_agency_oris()
    for ori in oris:
        print(ori)