import pytz

from datetime import datetime

from src.get_events_df import get_events_df

#def test_get_events_df_20260221():
#    assert len(get_events_df(datetime(2026,2,21))) == 2

#def test_get_events_df_20260213():
#    assert len(get_events_df(datetime(2026,2,13))) == 5

def test_get_events_df_20260319():
    events_df = get_events_df(datetime(2026,3,19))

    assert len(events_df) == 1

    assert events_df.loc[0,"event_start"].hour == 14
    assert events_df.loc[0,"event_start"].tzinfo.zone == pytz.timezone('America/Chicago').zone
