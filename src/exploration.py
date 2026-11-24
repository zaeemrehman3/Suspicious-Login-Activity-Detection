import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "raw" / "events.csv"

data = pd.read_csv(DATA_PATH)
print(data.info())