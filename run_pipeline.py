from pipeline.ingest import load_data
from pipeline.validate import validate_data
from pipeline.train import train_model
from pipeline.promote import promote
import os


def run(path: str):
    print("Loading data...")
    df = load_data(path)

    print("Validating data...")
    validate_data(df)

    X = df.drop("target", axis=1)
    y = df["target"]

    print("Training model...")
    train_model(X, y)

    print("Promoting model...")
    promote()

    print("Pipeline completed successfully")


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, "data", "sample.csv")
    run(data_path)