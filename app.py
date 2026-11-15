
from flask import Flask, request, jsonify

app = Flask(__name__)

todos = [
    {"id": 1, "task": "Complete DevOps project", "completed": False},
    {"id": 2, "task": "Learn Docker", "completed": True}
]

@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)

@app.route("/todos", methods=["POST"])
def add_todo():
    data = request.get_json()
    if not data or "task" not in data:
        return jsonify({"error": "Task is required"}), 400

    todo = {
        "id": len(todos) + 1,
        "task": data["task"],
        "completed": False
    }
    todos.append(todo)
    return jsonify(todo), 201

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
