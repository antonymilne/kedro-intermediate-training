import click
from kedro.framework.project import pipelines

from spaceflights.hooks import _inspect_func


@click.group()
def cli():
    pass


@cli.command()
def inspect():
    """Inspect the nodes in a pipeline."""
    nodes = pipelines["__default__"].nodes
    for node in nodes:
        node_name = node.name
        location, number_lines = _inspect_func(node.func)
        click.echo(
            f"`{node_name}` is defined at {location} and is {number_lines} lines long"
        )
