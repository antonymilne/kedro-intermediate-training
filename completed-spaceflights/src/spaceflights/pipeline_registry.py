"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline

from spaceflights.pipelines import data_filtering as df
from spaceflights.pipelines import data_processing as dp
from spaceflights.pipelines import data_science as ds


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.

    """
    data_processing_pipeline = dp.create_pipeline()
    data_science_pipeline = ds.create_pipeline()

    unfiltered_ds_pipeline = pipeline(
        data_science_pipeline, namespace="unfiltered", inputs={"model_input_table"}
    )

    data_filtering_pipeline = df.create_pipeline()

    filtered_ds_pipeline = (
        pipeline(
            data_filtering_pipeline,
            inputs={"input_table": "model_input_table"},
            outputs={"output_table": "filtered.model_input_table"},
            namespace="filtered",
        )
        + pipeline(data_science_pipeline, namespace="filtered")
    )

    return {
        "__default__": (
            data_processing_pipeline + unfiltered_ds_pipeline + filtered_ds_pipeline
        ),
        "dp": data_processing_pipeline,
        "ds": unfiltered_ds_pipeline + filtered_ds_pipeline,
        "filtered_pipeline": data_processing_pipeline + filtered_ds_pipeline,
        "unfiltered_pipeline": data_processing_pipeline + unfiltered_ds_pipeline,
    }


# EXTRA TODO 1: give data_processing_pipeline a namespace so that it can be
#  collapsed in kedro-viz. You will need to fix the inputs/outputs and/or edit the
#  names of the catalog entries to get a correctly connected pipeline.

# EXTRA TODO 2: run the data_filtering_pipeline twice in series to get model
#  performance after filtering by engine_type == "Quantum" AND then by
#  shuttle_type == "Type F5". You should do this just by altering this file and
#  parameters file without touching anything in pipelines/data_filtering.

# EXTRA TODO 3: run the data_filtering_pipeline onwards twice in parallel to get
#  model  performance after filtering by engine_type == "Quantum" OR by
#  shuttle_type == "Type F5". You should do this just by altering this file and
#  parameters file without touching anything in pipelines/data_filtering.
