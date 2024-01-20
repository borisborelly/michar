import click
from  michar.cli.app.michar import gooza
from michar.api.fbi.client import FBIClient

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
    oris = client.get_all_agency_oris()
    for ori in oris:
        print(ori)