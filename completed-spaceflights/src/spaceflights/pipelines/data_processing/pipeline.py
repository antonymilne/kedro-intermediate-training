from kedro.pipeline import pipeline, node

from .nodes import (
    create_model_input_table,
    preprocess_companies,
    preprocess_shuttles,
    get_top_company_locations,
)


def create_pipeline(**kwargs):
    return pipeline(
        [
            node(
                func=preprocess_companies,
                inputs="companies",
                outputs="preprocessed_companies",
                name="preprocess_companies_node",
            ),
            node(
                func=preprocess_shuttles,
                inputs="shuttles",
                outputs="preprocessed_shuttles",
                name="preprocess_shuttles_node",
            ),
            node(
                func=create_model_input_table,
                inputs=["preprocessed_shuttles", "preprocessed_companies", "reviews"],
                outputs="model_input_table",
                name="create_model_input_table_node",
            ),
            node(
                func=get_top_company_locations,
                inputs="preprocessed_companies",
                outputs="company_locations_plot",
                name="plot_top_company_locations_node",
            ),
        ]
    )
