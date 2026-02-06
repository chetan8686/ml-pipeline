import pandas as pd
import os


def load_data(path: str) -> pd.DataFrame:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Data file not found: {path}")

    df = pd.read_csv(path)

    if df.empty:
        raise ValueError("Loaded dataframe is empty")

    return df