#!/usr/bin/env python3
import argparse
import csv
import json
import os
import urllib.request
from pathlib import Path


def find_latest_csv() -> Path:
    candidates = sorted(Path("/workspace/output").glob("monitoring-*.csv"))
    if not candidates:
        raise FileNotFoundError("No monitoring-*.csv files found in /workspace/output")
    return candidates[-1]


def read_csv_rows(csv_path: Path) -> list[list[object]]:
    with csv_path.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.reader(fh)
        rows = list(reader)
    if not rows:
        return []
    data = []
    for row in rows[1:]:
        converted = []
        for idx, value in enumerate(row):
            if value == "":
                converted.append("")
            elif idx in {0, 1, 4, 6, 8, 10, 12, 14, 15}:
                converted.append(value)
            else:
                number = float(value)
                converted.append(int(number) if number.is_integer() else number)
        data.append(converted)
    return data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--webhook-url", default=os.environ.get("APPS_SCRIPT_WEBHOOK_URL"))
    parser.add_argument("--shared-secret", default=os.environ.get("APPS_SCRIPT_SHARED_SECRET"))
    parser.add_argument("--csv")
    args = parser.parse_args()

    if not args.webhook_url:
        raise SystemExit("--webhook-url or APPS_SCRIPT_WEBHOOK_URL is required")
    if not args.shared_secret:
        raise SystemExit("--shared-secret or APPS_SCRIPT_SHARED_SECRET is required")

    csv_path = Path(args.csv) if args.csv else find_latest_csv()
    rows = read_csv_rows(csv_path)
    payload = json.dumps(
        {"shared_secret": args.shared_secret, "rows": rows}, ensure_ascii=False
    ).encode("utf-8")
    req = urllib.request.Request(
        args.webhook_url,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        print(resp.read().decode("utf-8"))


if __name__ == "__main__":
    main()
