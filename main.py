import argparse
import os

from src.gen_cal_html import gen_cal_html

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Output file path")
    args = parser.parse_args()

    if os.path.dirname(args.path):
        os.makedirs(os.path.dirname(args.path), exist_ok=True)

    html = "<html>"
    html += gen_cal_html()
    html += "</html>"

    with open(args.path, "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    main()
