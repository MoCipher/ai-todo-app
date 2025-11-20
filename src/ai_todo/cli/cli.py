import click
from ai_todo.services import prioritization, reminders, speech

@click.group()
def cli():
    """AI-Powered To-Do List Command Line Interface."""
    pass

@cli.command()
@click.argument('task')
def add(task):
    """Add a new task to the to-do list."""
    # Logic to add the task
    click.echo(f'Task "{task}" added.')

@cli.command()
@click.argument('task_id')
def complete(task_id):
    """Mark a task as complete."""
    # Logic to mark the task as complete
    click.echo(f'Task {task_id} marked as complete.')

@cli.command()
def list():
    """List all tasks."""
    # Logic to list all tasks
    click.echo('Listing all tasks...')

@cli.command()
@click.argument('task_id')
@click.argument('priority')
def prioritize(task_id, priority):
    """Set the priority of a task."""
    # Logic to prioritize the task
    prioritization.set_priority(task_id, priority)
    click.echo(f'Task {task_id} priority set to {priority}.')

@cli.command()
@click.argument('task_id')
@click.argument('reminder_time')
def remind(task_id, reminder_time):
    """Set a reminder for a task."""
    reminders.set_reminder(task_id, reminder_time)
    click.echo(f'Reminder set for task {task_id} at {reminder_time}.')

@cli.command()
def voice():
    """Add or update tasks using voice commands."""
    speech.handle_voice_commands()

if __name__ == '__main__':
    cli()