from taskboard.tasks import sort_by_priority


def test_priority_sort_keeps_equal_and_unknown_priorities_stable():
    tasks = [
        {"id": 1, "priority": "low"},
        {"id": 2, "priority": "urgent"},
        {"id": 3, "priority": "backlog"},
        {"id": 4, "priority": "high"},
        {"id": 5, "priority": "high"},
    ]
    assert [task["id"] for task in sort_by_priority(tasks)] == [2, 4, 5, 1, 3]
