import pandas as pd
from pathlib import Path

# Resolve path relative to project root
DATA_DIR = Path(__file__).resolve().parent.parent / "data"

def load_unified_data():
    """Load the main Ethiopia financial inclusion dataset from Excel."""
    df = pd.read_excel(
        DATA_DIR / "raw" / "ethiopia_fi_unified_data.xlsx",
        parse_dates=["observation_date"],   # only parse columns that exist
        engine="openpyxl"
    )
    return df

def load_reference_codes():
    """Load the reference codes dataset from Excel."""
    df = pd.read_excel(
        DATA_DIR / "raw" / "reference_codes.xlsx",
        engine="openpyxl"
    )
    return df
