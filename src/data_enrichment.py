import pandas as pd
from datetime import datetime

COLLECTED_BY = "Azeb Mehrete"
COLLECTION_DATE = datetime.today().date()

def add_enrichment_records(df):
    new_records = []

    # 🔹 Observation: Smartphone penetration
    new_records.append({
        "record_type": "observation",
        "pillar": "enabler",
        "indicator": "Smartphone penetration",
        "indicator_code": "ENB_SMARTPHONE_PCT",
        "value_numeric": 44.0,
        "observation_date": "2024-01-01",
        "source_name": "GSMA",
        "source_url": "https://www.gsma.com",
        "confidence": "medium",
        "original_text": "Smartphone adoption in Ethiopia reached approximately 44% in 2024.",
        "collected_by": COLLECTED_BY,
        "collection_date": COLLECTION_DATE,
        "notes": "Key enabler for digital payments"
    })

    # 🔹 Event: Fayda Digital ID rollout
    new_records.append({
        "record_type": "event",
        "category": "infrastructure",
        "event_date": "2023-10-01",
        "source_name": "Ethiopian Digital ID",
        "source_url": "https://id.gov.et",
        "confidence": "high",
        "original_text": "National rollout of Fayda Digital ID.",
        "collected_by": COLLECTED_BY,
        "collection_date": COLLECTION_DATE,
        "notes": "Reduces KYC friction for account opening"
    })

    # 🔹 Impact link
    new_records.append({
        "record_type": "impact_link",
        "parent_id": "EVENT_FAYDA_ID",
        "pillar": "access",
        "related_indicator": "ACC_OWNERSHIP",
        "impact_direction": "positive",
        "impact_magnitude": 1.5,
        "lag_months": 12,
        "evidence_basis": "Comparable impact observed in India Aadhaar rollout"
    })

    return pd.concat([df, pd.DataFrame(new_records)], ignore_index=True)
