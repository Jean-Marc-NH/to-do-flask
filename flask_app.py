from flask import Flask, render_template, request
from uuid import uuid4

app = Flask(__name__)

task = {

}


@app.route('/',  methods=["POST", "GET"])
def index():

    if request.form.get('act1') == 'add':
        x = request.form.get('tarea')
        if x != None:
            task[str(uuid4())] = x
    elif  request.form.get('act2') == 'del':
        task.clear  ()
    elif 'sup' in request.form:
        key = request.form['sup']
        del task[key]
    return render_template('index.html', task = task)
