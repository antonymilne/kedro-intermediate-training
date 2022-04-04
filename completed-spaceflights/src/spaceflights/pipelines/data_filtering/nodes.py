from typing import Dict, Any

import pandas as pd


def filter_data(data: pd.DataFrame, filter_params: Dict[str, Any]) -> pd.DataFrame:
    mask = data[filter_params["column"]] == filter_params["value"]
    return data[mask]
