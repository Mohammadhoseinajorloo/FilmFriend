import pandas as pd


def calculate_quartile_tag(table: pd.DataFrame) -> pd.DataFrame:
    return table.groupby("userId").count()
