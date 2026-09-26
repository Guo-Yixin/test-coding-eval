from taskboard.tasks import filter_by_status


def test_status_filter_is_case_insensitive_and_does_not_mutate_tasks():
    tasks = [
        {"id": 1, "status": "open"},
        {"id": 2, "status": "done"},
        {"id": 3, "status": "OPEN"},
    ]
    original = [dict(task) for task in tasks]

    assert [task["id"] for task in filter_by_status(tasks, "Open")] == [1, 3]
    assert tasks == original


def test_status_filter_returns_empty_list_when_no_task_matches():
    assert filter_by_status([{"status": "open"}], "blocked") == []
