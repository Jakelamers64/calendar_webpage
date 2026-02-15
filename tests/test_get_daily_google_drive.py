from datetime import datetime

from src.get_daily_google_drive import get_daily_google_drive

def test_get_daily_google_drive_20260223():
    assert len(get_daily_google_drive(datetime(2026,2,23))) == 1
