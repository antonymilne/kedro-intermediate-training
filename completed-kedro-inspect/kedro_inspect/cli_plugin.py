import click
from kedro.framework.project import pipelines
from .plugin import _inspect_func


@click.group(name="kedro-inspect")
def inspect_cli():
    pass

@inspect_cli.command()
def inspect():
    """Inspect the nodes in a pipeline."""
    nodes = pipelines["__default__"].nodes
    for node in nodes:
        location, number_lines = _inspect_func(node.func)
        node_name = node.name
        click.echo(
            f"`{node_name}`` defined at {location} and is {number_lines} lines long"
        )
