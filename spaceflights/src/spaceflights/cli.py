from kedro.framework.project import pipelines
from spaceflights.hooks import _inspect_func


@cli.command()
def inspect():
    """Inspect the nodes in a pipeline."""
    nodes = pipelines["__default__"].nodes
    # TODO: For each node use click.echo to output the inspection result to the console.
