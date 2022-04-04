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
        if "no_inspect" in node.tags:
            return
        node_name = node.name
        location, number_lines = _inspect_func(node.func)
        log.info(
            f"`{node_name}` is defined at {location} and is {number_lines} lines long"
        )

    @hook_impl
    def after_dataset_loaded(self, dataset_name: str, data: Any) -> None:
        if isinstance(data, pd.DataFrame):
            log.info(f"{dataset_name} has shape {data.shape}")


def _inspect_func(func: Callable) -> Tuple[str, int]:
    """Gives the location (file and line number) and number of lines in `func`."""
    file = inspect.getsourcefile(func)
    lines, first_line = inspect.getsourcelines(func)
    location = f"{file}:{first_line}"
    return location, len(lines)


def _inspect_func(func: Callable) -> Tuple[str, int]:
    """Gives the location (file and line number) and number of lines in `func`."""
    file = inspect.getsourcefile(func)
    lines, first_line = inspect.getsourcelines(func)
    location = f"{file}:{first_line}"
    return location, len(lines)
