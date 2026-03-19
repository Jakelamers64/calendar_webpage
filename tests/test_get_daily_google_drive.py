import pytz

from datetime import datetime

from src.get_daily_google_drive import get_daily_google_drive

def test_get_daily_google_drive_20260223():
    assert len(get_daily_google_drive(datetime(2026,2,23))) == 2

def test_get_daily_google_drive_20260319():
    events_2026_03_19 = get_daily_google_drive(datetime(2026,3,19))

    assert len(events_2026_03_19)

    assert events_2026_03_19[0]["event_start"].hour == 14
    assert events_2026_03_19[0]["event_end"].hour == 15
    assert events_2026_03_19[0]["event_start"].tzinfo.zone == pytz.timezone('America/Chicago').zone
