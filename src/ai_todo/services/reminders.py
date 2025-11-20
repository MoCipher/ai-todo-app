from datetime import datetime, timedelta
import json

class Reminder:
    def __init__(self, task_id, reminder_time):
        self.task_id = task_id
        self.reminder_time = reminder_time
        self.is_active = True

    def deactivate(self):
        self.is_active = False

class ReminderService:
    def __init__(self):
        self.reminders = []

    def set_reminder(self, task_id, reminder_time):
        reminder = Reminder(task_id, reminder_time)
        self.reminders.append(reminder)
        return reminder

    def get_active_reminders(self):
        return [reminder for reminder in self.reminders if reminder.is_active]

    def check_reminders(self):
        current_time = datetime.now()
        for reminder in self.reminders:
            if reminder.is_active and reminder.reminder_time <= current_time:
                self.send_reminder(reminder)
                reminder.deactivate()

    def send_reminder(self, reminder):
        # Placeholder for sending reminder notification
        print(f"Reminder: Task {reminder.task_id} is due at {reminder.reminder_time.strftime('%Y-%m-%d %H:%M:%S')}")

    def load_reminders(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                for item in data:
                    reminder = Reminder(item['task_id'], datetime.fromisoformat(item['reminder_time']))
                    self.reminders.append(reminder)
        except Exception as e:
            print(f"Error loading reminders: {e}")

    def save_reminders(self, file_path):
        try:
            with open(file_path, 'w') as file:
                data = [{'task_id': reminder.task_id, 'reminder_time': reminder.reminder_time.isoformat()} for reminder in self.reminders]
                json.dump(data, file)
        except Exception as e:
            print(f"Error saving reminders: {e}")