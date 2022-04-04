from kedro.pipeline import pipeline, node

from .nodes import filter_data


def create_pipeline(**kwargs):
    return pipeline(
        [
            node(
                func=filter_data,
                inputs=["input_table", "params:filter"],
                outputs="output_table",
            )
        ]
    )
