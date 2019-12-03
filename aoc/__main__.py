import logging

import click

log = logging.getLogger(__name__)

@click.group
@click.option('--verbose/--no-verbose', '-v', default=False)
def cli(verbose):
    if verbose:
        log.setLevel(logging.DEBUG)

@cli.command()
@click.argument('day', type=int)
def run(day):
    pass

