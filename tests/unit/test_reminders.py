import unittest
from src.ai_todo.services.reminders import set_reminder, get_reminders, delete_reminder

class TestReminders(unittest.TestCase):

    def setUp(self):
        self.reminders = []

    def test_set_reminder(self):
        reminder = set_reminder("Test task", "2023-10-10 10:00:00")
        self.reminders.append(reminder)
        self.assertEqual(len(self.reminders), 1)
        self.assertEqual(self.reminders[0]['task'], "Test task")
        self.assertEqual(self.reminders[0]['time'], "2023-10-10 10:00:00")

    def test_get_reminders(self):
        set_reminder("Test task 1", "2023-10-10 10:00:00")
        set_reminder("Test task 2", "2023-10-11 11:00:00")
        reminders = get_reminders()
        self.assertEqual(len(reminders), 2)

    def test_delete_reminder(self):
        reminder = set_reminder("Test task", "2023-10-10 10:00:00")
        self.reminders.append(reminder)
        delete_reminder(reminder['id'])
        self.assertEqual(len(self.reminders), 0)

if __name__ == '__main__':
    unittest.main()