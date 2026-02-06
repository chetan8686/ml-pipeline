import os
import shutil


def promote():
    src = "models/candidate/model.pkl"
    dst = "models/production/model.pkl"

    if not os.path.exists(src):
        raise FileNotFoundError("No candidate model found to promote")

    os.makedirs("models/production", exist_ok=True)

    shutil.copy(src, dst)