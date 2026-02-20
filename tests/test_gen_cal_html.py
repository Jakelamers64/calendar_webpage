from datetime import datetime

from src.gen_cal_html import gen_cal_html

def test_gen_cal_html_20260221():
    html = gen_cal_html(datetime(2026,2,23))

    print(html)

    # Check google event
    google_drive_html = "<div class='mcw-event-div'>Dialysis Clinic<br>Children's Dialysis Clinic</div>"

    assert google_drive_html in html

    # Check mcw event
    mcw_event_html = """<td class='time-cell'>08:00 - 08:15</td>
			<td class='schedule-cell'><div class='mcw-event-div'>Resp - WEBCAST: Intro to Patient of the Week<br>Rooms on Your Own </div></td>
			<td class='actual-cell'></td>"""

    assert mcw_event_html in html
