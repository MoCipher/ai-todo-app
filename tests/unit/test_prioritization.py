import unittest
from ai_todo.services.prioritization import prioritize_tasks

class TestTaskPrioritization(unittest.TestCase):

    def test_prioritize_tasks_basic(self):
        tasks = [
            {"id": 1, "description": "Task 1", "priority": 2},
            {"id": 2, "description": "Task 2", "priority": 1},
            {"id": 3, "description": "Task 3", "priority": 3},
        ]
        prioritized = prioritize_tasks(tasks)
        self.assertEqual(prioritized[0]["id"], 2)
        self.assertEqual(prioritized[1]["id"], 1)
        self.assertEqual(prioritized[2]["id"], 3)

    def test_prioritize_tasks_empty(self):
        tasks = []
        prioritized = prioritize_tasks(tasks)
        self.assertEqual(prioritized, [])

    def test_prioritize_tasks_same_priority(self):
        tasks = [
            {"id": 1, "description": "Task 1", "priority": 1},
            {"id": 2, "description": "Task 2", "priority": 1},
        ]
        prioritized = prioritize_tasks(tasks)
        self.assertIn({"id": 1, "description": "Task 1", "priority": 1}, prioritized)
        self.assertIn({"id": 2, "description": "Task 2", "priority": 1}, prioritized)

if __name__ == '__main__':
    unittest.main()