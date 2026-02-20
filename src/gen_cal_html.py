import math
import os
import pytz

from datetime import datetime
#from tqdm import tqdm

from src.get_events_df import get_events_df

def get_event_str_for_15_min(block_start_time, block_end_time, events_df, date=datetime.today()):
    """
    returns a str for events based on the time
    """

    block_html = ""

    for i, event in events_df.iterrows():
        if event["event_start"] <= block_start_time and event["event_end"] > block_start_time:
            block_html = str(block_html) + "<div class='mcw-event-div'>" + str(event["event_title"]) + "<br>" + str(event["event_loc"]) + "</div>"
    
    return block_html


def gen_cal_html(date=datetime.today()):
    """
    Creates an html page that is a calender with 15 min units
    that have all activites scheduled in mcw oasis and google
    drive for that block

    :returns: event html as a str
    """

    css_path = f"{os.path.expanduser("~")}/Documents/Code/python/calendar_webpage/assests/css/calendar_style.css"

    with open(css_path, "r", encoding="utf-8") as f:
        css_string = f.read().replace("\n", "\n\t\t")

    html = f"""
    \t<style>
    {css_string}
    \t</style>
    \t<table class='schedule-table'>
    \t\t<tr>
    \t\t\t<td>Time</td>
    \t\t\t<td class='table-cell'>Schedule</td>
    \t\t\t<td class='table-cell'>Actual</td>
    \t\t</tr> 
    """
    events_df = get_events_df(date)

    #print(events_df)

    for i in range(0,24*4):
        block_start_time = date.replace(
                    hour=(math.floor(i/4)),
                    minute=((i%4)*15),
                    tzinfo=pytz.timezone('America/Chicago')
                )

        # @TODO Hand midnight end of day
        block_end_time = date.replace(
                    hour=(math.floor((i+1)/4)) % 24,
                    minute=(((i+1)%4)*15),
                    tzinfo=pytz.timezone('America/Chicago')
                )
    

        html += "\t\t<tr>\n"
        html += f"\t\t\t<td class='time-cell'>{block_start_time.strftime('%H:%M')} - {block_end_time.strftime('%H:%M')}</td>\n"
        html += f"\t\t\t<td class='schedule-cell'>{get_event_str_for_15_min(block_start_time,block_end_time,events_df)}</td>\n"
        html += "\t\t\t<td class='actual-cell'></td>\n"
        html += "\t\t</tr>\n"

    html += "\t</table>\n"

    return html
