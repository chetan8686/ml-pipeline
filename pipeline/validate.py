def validate_data(df):
    if df.empty:
        raise ValueError("Input data is empty")

    if "target" not in df.columns:
        raise ValueError("Missing target column")