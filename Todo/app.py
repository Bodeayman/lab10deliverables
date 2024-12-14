from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []
#We start in our application with an empty list


# These functions for adding or reading the tasks
def add_task(task):
    tasks.append(task)

def get_tasks():
    return tasks

@app.route('/')
def index():
    #The index2 will get tasks and uses it inside the webpage
    return render_template('index2.html', tasks=get_tasks())

@app.route('/add-task', methods=['POST'])
def add_task_route():
    
    # take the data from the form in the addtask file
    task = request.form.get('task')
    if task:
        add_task(task)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
