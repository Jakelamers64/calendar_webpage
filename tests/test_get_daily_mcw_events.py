import pytz

from datetime import datetime

from src.get_daily_mcw_events import get_daily_mcw_events

def test_get_daily_mcw_events_sat_20260214():
    """
    Test to check if a weekend date with no mcw events returns 
    a list with no elements.
    """
    assert len(get_daily_mcw_events(datetime(2026,2,14))) == 0

def test_get_daily_mcw_events_fri_20260213():
    """
    Tests to see if a week day with 4 events returns a list
    of four events.
    """
    assert len(get_daily_mcw_events(datetime(2026,2,13))) == 4

def test_get_daily_mcw_events_wed_20260218():
    """
    Checks that a wednesday returns a list with the correct number of
    elements and the correct times
    """
    events = get_daily_mcw_events(datetime(2026,2,18))

    assert len(events) == 5

    # PBD
    assert events[0]["event_start"] == datetime(2026,2,18,8,0,tzinfo=pytz.timezone('America/Chicago'))
    assert events[0]["event_end"] == datetime(2026,2,18,10,0,tzinfo=pytz.timezone('America/Chicago'))

    # TGD
    assert events[1]["event_start"] == datetime(2026,2,18,10,0,tzinfo=pytz.timezone('America/Chicago'))
    assert events[1]["event_end"] == datetime(2026,2,18,12,0,tzinfo=pytz.timezone('America/Chicago'))

    # Climb
    assert events[2]["event_start"] == datetime(2026,2,18,13,tzinfo=pytz.timezone('America/Chicago'))
    assert events[2]["event_end"] == datetime(2026,2,18,17,tzinfo=pytz.timezone('America/Chicago'))
