import pytz
import pandas as pd

from datetime import datetime

def get_daily_google_drive(date=datetime.today()):
    """
    Get all events from a google sheet for today

    :returns: a list of event jsons:
        (start_time, end_time, event_title, event_sum, event_loc)

    Link to the sheet:
    https://docs.google.com/spreadsheets/d/1JnGfqPFGsKdM3HeDIfKrqM4-33PkxCMW7YH-PoAPZkY/edit?usp=sharing
    """
    gsheetkey = "1JnGfqPFGsKdM3HeDIfKrqM4-33PkxCMW7YH-PoAPZkY" 

    sheet_name = 'Form Responses 1'

    url = f'https://docs.google.com/spreadsheet/ccc?key={gsheetkey}&output=xlsx'
    events_df = pd.read_excel(url,sheet_name=sheet_name)

    # Debug
    #print(events_df)

    events = []

    for i, row in events_df.iterrows():
        if row["Event Date"].date() == date.date():
            start_time = row['Event Date'].replace(
                        hour=row['Event Start Time'].hour,
                        minute=row['Event Start Time'].minute,
                        second=row['Event Start Time'].second,
                        tzinfo=pytz.timezone('America/Chicago')
                    )

            end_time = row['Event Date'].replace(
                        hour=row['Event End Time'].hour,
                        minute=row['Event End Time'].minute,
                        second=row['Event End Time'].second,
                        tzinfo=pytz.timezone('America/Chicago')
                    )
            
            events.append({
                    "event_cat":f"google/{row['Event Category']}/{row['Sub Category']}",
                    "event_start":start_time,
                    "event_end":end_time,
                    "event_title":row["Event Title"],
                    "event_sum":row["Event Description"],
                    "event_loc":row["Event Location"]
                })

    return events
