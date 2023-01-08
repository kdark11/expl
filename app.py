from flask import Flask, render_template, flash, redirect, url_for
from forms import TaskForm
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = TaskForm()
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        # Save the task to the database
        flash('Task created successfully')
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run()
