from taskboard.tasks import filter_by_status, search_tasks, sort_by_priority


TASKS = [
    {"id": 1, "title": "Write docs", "status": "open", "priority": "low"},
    {"id": 2, "title": "Fix API", "status": "done", "priority": "high"},
]


def test_no_status_filter_returns_all_tasks_without_mutating_input():
    original = list(TASKS)
    assert filter_by_status(TASKS) == TASKS
    assert TASKS == original


def test_empty_search_returns_all_tasks():
    assert search_tasks(TASKS, "") == TASKS


def test_priority_sort_orders_known_priorities():
    assert [task["id"] for task in sort_by_priority(TASKS)] == [2, 1]
