from __future__ import absolute_import

import click
from .render import render
from .build import build
from .test import test


@click.group()
def cli():
    pass


cli.add_command(render)
cli.add_command(build)
cli.add_command(test)
