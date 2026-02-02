REQUIRED_COLUMNS = [
    "record_id",
    "record_type",
    "pillar",
    "indicator",
    "indicator_code",
    "value_numeric",
    "observation_date",
    "category",
    "source_name",
    "source_url",
    "confidence"
]

def validate_schema(df):
    missing = set(REQUIRED_COLUMNS) - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    print("✅ Schema validation passed. All required columns are present.")
