from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def view_tasks(self):
        return self.tasks

    def complete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            return True
        return False

todo_list = ToDoList()

@app.route('/')
def home():
    tasks = todo_list.view_tasks()
    return render_template_string('''
        <!doctype html>
        <title>To-Do List</title>
        <h1>To-Do Executive List</h1>
        <form action="/add" method="post">
            <input type="text" name="task" placeholder="Enter a new task">
            <input type="submit" value="Add Task">
        </form>
        <h2>Tasks</h2>
        <ul>
        {% for idx, task in enumerate(tasks) %}
            <li>{{ idx + 1 }}. {{ task['task'] }} - {{ 'Completed' if task['completed'] else 'Not completed' }}
                <form action="/complete/{{ idx }}" method="post" style="display:inline;">
                    <button type="submit">Complete</button>
                </form>
            </li>
        {% endfor %}
        </ul>
    ''', tasks=tasks, enumerate=enumerate)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    todo_list.add_task(task)
    return redirect(url_for('home'))

@app.route('/complete/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    if todo_list.complete_task(task_id + 1):
        return redirect(url_for('home'))
    return 'Invalid task ID', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)







