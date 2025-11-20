from flask import Blueprint, request, jsonify
from ..services.prioritization import prioritize_tasks
from ..services.reminders import set_reminder, get_reminders
from ..schemas.task import TaskSchema

api = Blueprint('api', __name__)

@api.route('/tasks', methods=['POST'])
def add_task():
    task_data = request.json
    task_schema = TaskSchema()
    if task_schema.validate(task_data):
        # Logic to add task to the database
        return jsonify({"message": "Task added successfully"}), 201
    return jsonify({"error": "Invalid task data"}), 400

@api.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task_data = request.json
    # Logic to update task in the database
    return jsonify({"message": "Task updated successfully"}), 200

@api.route('/tasks', methods=['GET'])
def get_tasks():
    # Logic to retrieve tasks from the database
    return jsonify({"tasks": []}), 200

@api.route('/tasks/prioritize', methods=['POST'])
def prioritize():
    tasks = request.json.get('tasks', [])
    prioritized_tasks = prioritize_tasks(tasks)
    return jsonify({"prioritized_tasks": prioritized_tasks}), 200

@api.route('/reminders', methods=['POST'])
def create_reminder():
    reminder_data = request.json
    if set_reminder(reminder_data):
        return jsonify({"message": "Reminder set successfully"}), 201
    return jsonify({"error": "Failed to set reminder"}), 400

@api.route('/reminders', methods=['GET'])
def list_reminders():
    reminders = get_reminders()
    return jsonify({"reminders": reminders}), 200