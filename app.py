from flask import Flask, render_template
from forms import TaskForm
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)

@app.route('/')
def index():
    form = TaskForm()
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run()
