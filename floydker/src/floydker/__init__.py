from __future__ import absolute_import

import click
from .render import render


@click.group()
def cli():
    pass

cli.add_command(render)
