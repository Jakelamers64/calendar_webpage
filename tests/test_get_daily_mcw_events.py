from datetime import datetime

from src.get_daily_mcw_events import get_daily_mcw_events

def test_get_daily_mcw_events_sat_20260214():
    dt_sat = datetime(2026,2,14)

    assert len(get_daily_mcw_events(dt_sat)) == 0

def test_get_daily_mcw_events_fri_20260213():
    dt_fri = datetime(2026,2,13)

    assert len(get_daily_mcw_events(dt_fri)) == 4
