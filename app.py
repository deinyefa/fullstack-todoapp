# import psycopg2
from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://deiny@localhost:5432/todoapp'
db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id}, {self.description}>'


db.create_all()


@app.route('/todos/create', methods=['POST'])
def create_todo():
    # get the input user sent
    description = request.get_json()['description']
    # create a new pending addition to todos table
    todo = Todo(description=description)
    db.session.add(todo)
    # commit that to the db
    db.session.commit()
    # redirect user back to index page
    return jsonify({
        'description': todo.description
    })


@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all())
