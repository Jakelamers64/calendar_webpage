import pandas as pd

from datetime import datetime

from src.get_daily_mcw_events import get_daily_mcw_events
from src.get_daily_google_drive import get_daily_google_drive

def get_events_df(date=datetime.today()):
    """
    Combines a list of jsons from different event db
    into one pandas df for all df for that day

    :returns: A df containing events with the following
    headers; ("event_cat","event_start", "event_end","event_title","event_sum","event_loc")
    """
    events_df = pd.DataFrame(
                columns = [
                        "event_cat",
                        "event_start",
                        "event_end",
                        "event_title",
                        "event_sum",
                        "event_loc"
                    ])

    for event in get_daily_mcw_events(date):
        events_df = pd.concat([events_df,pd.DataFrame([event])], ignore_index=True)

    for event in get_daily_google_drive(date):
        events_df = pd.concat([events_df,pd.DataFrame([event])], ignore_index=True)

    print(events_df)

    return events_df

