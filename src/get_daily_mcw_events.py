import pytz
import requests

from icalendar import Calendar
from datetime import datetime

#def standardize_date(datetime_to_standardize):
#    """
#    Sets all dt data to zero other than date and standardizes
#    the timezone for date comparsions
#
#    :return: datetime with just dates as nonzero
#    """
#    return datetime_to_standardize.replace(
#                hour=0, 
#                minute=0, 
#                second=0, 
#                microsecond=0,
#                tzinfo=pytz.timezone('America/Chicago')
#            )


def get_daily_mcw_events(date=datetime.today()):
    """
    Gets all daily events from mcw oasis calendar

    :return: A list of event jsons where each json has; 
        (event_start, event_end, event_title, event_sum, event_loc)
    """

    # Should move this to a config file
    # Should make a dic so I can convert between code and class name
    current_classes = [
                "INTE-12102", #Climb
                "PWAY-12210", #UCH
                "INTE-12104", #TGD
                "INTE-11106", #Resp
                "INTE-11107", #Renal
                "INTE-11108", #EndoRepro
                "INTE-11109"  #Nuero (Guess)
            ]
    
    # Should move this to a config file
    r = requests.get('https://oasis.acad.mcw.edu/calendar/m=9&m=29&m=3&m=5&m=11&m=23&m=24&m=25&m=26&m=28&m=12&m=16&m=27&m=8&m=6&m=30&m=14&m=10&m=4&module_name=Multiple%20Modules&export_to=gcal&export_length=7&yid=2026')

    calendar = Calendar.from_ical(r.text.encode('utf-8'))

    events = []

    # Extract events
    for component in calendar.walk():
        if component.name == "VEVENT":
            if (
                    sum([current_class in str(component.get('description')) for current_class in current_classes]) > 0 and
                    'GB' not in str(component.get('description')) and
                    'CW' not in str(component.get('description')) and
                    'PANOPTO' not in str(component.get('summary'))
                ):
                #event_date = standardize_date(component.get('dtstart').dt)
                #today_date = standardize_date(date)

                if component.get('dtstart').dt.date() == date.date():
                    events.append({
                            "event_cat": f"mcw/{ current_classes[[current_class in str(component.get('description')) for current_class in current_classes].index(True)]}",
                            "event_start": component.get('dtstart').dt.astimezone(pytz.timezone('America/Chicago')),
                            "event_end": component.get('dtend').dt.astimezone(pytz.timezone('America/Chicago')),
                            "event_title": component.get('summary'),
                            "event_sum": "@TODO",
                            "event_loc": component.get('LOCATION')
                        })

    return events
