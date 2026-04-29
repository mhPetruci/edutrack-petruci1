import sys
import json
from datetime import datetime, timezone


def parse_iso_datetime(value):
    if not value:
        return None

    try:
        dt = datetime.fromisoformat(value)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except ValueError:
        return None


def is_overdue(task):
    due_date = parse_iso_datetime(task.get("due_date"))
    if due_date is None:
        return False

    completed_at = parse_iso_datetime(task.get("completed_at"))
    status = (task.get("status") or "").strip().lower()

    if completed_at is not None or status == "completed":
        return False

    now = datetime.now(timezone.utc)
    return due_date < now


def find_overdue_subject_ids(tasks):
    overdue_ids = set()
    for task in tasks:
        subject_id = task.get("subject_id")
        if subject_id and is_overdue(task):
            overdue_ids.add(subject_id)
    return list(overdue_ids)


def main():
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        print(json.dumps([]))
        sys.exit(0)

    if not isinstance(payload, list):
        print(json.dumps([]))
        sys.exit(0)

    overdue_subject_ids = find_overdue_subject_ids(payload)
    print(json.dumps(overdue_subject_ids))


if __name__ == "__main__":
    main()
