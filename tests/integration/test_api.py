import pytest
from flask import json
from ai_todo.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_add_task(client):
    response = client.post('/api/tasks', json={
        'title': 'Test Task',
        'description': 'This is a test task',
        'priority': 'high'
    })
    assert response.status_code == 201
    data = json.loads(response.data)
    assert 'id' in data

def test_get_tasks(client):
    response = client.get('/api/tasks')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)

def test_update_task(client):
    response = client.post('/api/tasks', json={
        'title': 'Update Task',
        'description': 'This task will be updated',
        'priority': 'medium'
    })
    task_id = json.loads(response.data)['id']
    
    response = client.put(f'/api/tasks/{task_id}', json={
        'title': 'Updated Task',
        'description': 'This task has been updated',
        'priority': 'low'
    })
    assert response.status_code == 200
    updated_data = json.loads(response.data)
    assert updated_data['title'] == 'Updated Task'

def test_delete_task(client):
    response = client.post('/api/tasks', json={
        'title': 'Delete Task',
        'description': 'This task will be deleted',
        'priority': 'low'
    })
    task_id = json.loads(response.data)['id']
    
    response = client.delete(f'/api/tasks/{task_id}')
    assert response.status_code == 204

    response = client.get(f'/api/tasks/{task_id}')
    assert response.status_code == 404