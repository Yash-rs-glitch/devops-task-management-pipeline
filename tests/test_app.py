import app as application

def setup_function():
    application.todos.clear()
    application.todos.extend([
        {"id": 1, "task": "Complete DevOps project", "completed": False},
        {"id": 2, "task": "Learn Docker", "completed": True}
    ])

def test_get_todos():
    client = application.app.test_client()
    response = client.get("/todos")
    assert response.status_code == 200
    assert len(response.json) == 2

def test_add_todo():
    client = application.app.test_client()
    response = client.post("/todos", json={"task": "Learn Kubernetes"})
    assert response.status_code == 201
    assert response.json["task"] == "Learn Kubernetes"

def test_health():
    client = application.app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"