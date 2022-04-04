import logging
import time
from typing import Callable, Tuple, Any

from kedro.framework.hooks import hook_impl
from kedro.pipeline.node import Node

log = logging.getLogger(__name__)


class TimeDatasetLoadingHooks:
    def __init__(self):
        self._start_times = {}

    @hook_impl
    def before_dataset_loaded(self, dataset_name: str) -> None:
        self._start_times[dataset_name] = time.time()

    @hook_impl
    def after_dataset_loaded(self, dataset_name: str) -> None:
        elapsed_time = time.time() - self._start_times[dataset_name]
        log.info(f"Loading `{dataset_name}` took {elapsed_time:.3} seconds")


import inspect
import pandas as pd


class InspectHooks:
    @hook_impl
    def before_node_run(self, node: Node) -> None:
        node_name, location, number_lines = None, None, None
        # TODO: Find the real value of each of the above variables.
        #  Use _inspect_func to find location and number_lines.
        #  Do not print the information if the node is tagged with "no_inspect".
        log.info(
            f"`{node_name}` defined at {location} and is {number_lines} lines long"
        )

    @hook_impl
    def after_dataset_loaded(self, dataset_name: str, data: Any) -> None:
        # TODO: Log the shape of the dataset if it is a pandas DataFrame.
        pass


def _inspect_func(func: Callable) -> Tuple[str, int]:
    """Gives the location (file and line number) and number of lines in `func`."""
    file = inspect.getsourcefile(func)
    lines, first_line = inspect.getsourcelines(func)
    location = f"{file}:{first_line}"
    return location, len(lines)
