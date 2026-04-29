import argparse
import json


def calculate_progress(tasks):
    """Calculate progress percentage for a list of academic tasks.

    Each task is expected to be a dict containing at least a `status` field.
    The returned JSON structure includes completed, total, and progress_percentage.
    """
    if not isinstance(tasks, list):
        raise ValueError("tasks must be a list")

    total = len(tasks)
    completed = 0
    for task in tasks:
        if not isinstance(task, dict):
            continue
        status = task.get("status")
        if isinstance(status, str) and status.strip().lower() == "completed":
            completed += 1

    progress_percentage = round((completed / total) * 100, 2) if total else 0.0
    return {
        "completed": completed,
        "total": total,
        "progress_percentage": progress_percentage,
    }


def load_tasks_from_file(path):
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, list):
        raise ValueError("Input JSON must contain a list of tasks")
    return data


def main():
    parser = argparse.ArgumentParser(
        description="Calculate academic task progress and return JSON."
    )
    parser.add_argument(
        "--input-file",
        required=True,
        help="Path to a JSON file containing a list of tasks",
    )
    args = parser.parse_args()

    tasks = load_tasks_from_file(args.input_file)
    result = calculate_progress(tasks)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
