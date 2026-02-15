from datetime import datetime

from src.get_events_df import get_events_df

def test_get_events_df_20260221():
    assert len(get_events_df(datetime(2026,2,21))) == 2

def test_get_events_df_20260213():
    assert len(get_events_df(datetime(2026,2,13))) == 5
