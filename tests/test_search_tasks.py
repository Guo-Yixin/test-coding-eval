from taskboard.tasks import search_tasks


def test_search_is_case_insensitive_and_preserves_order():
    tasks = [
        {"id": 1, "title": "Fix API timeout"},
        {"id": 2, "title": "Write API docs"},
        {"id": 3, "title": "Clean UI"},
    ]
    assert [task["id"] for task in search_tasks(tasks, "api")] == [1, 2]


def test_search_ignores_tasks_without_a_title():
    assert search_tasks([{"id": 1}, {"id": 2, "title": "API"}], "api") == [{"id": 2, "title": "API"}]
