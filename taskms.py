from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': 'Task 1',
        'description': 'Description of Task 1',
        'due_date': '2023-06-30',
        'assigned_to': 'John',
        'completed': False
    },
    {
        'id': 2,
        'title': 'Task 2',
        'description': 'Description of Task 2',
        'due_date': '2023-07-15',
        'assigned_to': 'Jane',
        'completed': True
    }
]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/tasks/new', methods=['GET', 'POST'])
def create_task():
    if request.method == 'POST':
        new_task = {
            'id': len(tasks) + 1,
            'title': request.form['title'],
            'description': request.form['description'],
            'due_date': request.form['due_date'],
            'assigned_to': request.form['assigned_to'],
            'completed': False
        }
        tasks.append(new_task)
        return redirect('/')
    return render_template('create_task.html')

@app.route('/tasks/<int:task_id>/edit', methods=['GET', 'POST'])
def edit_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return redirect('/')
    if request.method == 'POST':
        task['title'] = request.form['title']
        task['description'] = request.form['description']
        task['due_date'] = request.form['due_date']
        task['assigned_to'] = request.form['assigned_to']
        return redirect('/')
    return render_template('edit_task.html', task=task)

@app.route('/tasks/<int:task_id>/complete', methods=['POST'])
def complete_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return redirect('/')
    task['completed'] = not task['completed']
    return redirect('/')

@app.route('/tasks/<int:task_id>/delete', methods=['POST'])
def delete_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return redirect('/')
    tasks.remove(task)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
