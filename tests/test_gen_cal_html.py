from datetime import datetime

from src.gen_cal_html import gen_cal_html

def test_gen_cal_html_20260221():
    print(gen_cal_html(datetime(2026,2,21)))

    assert False
