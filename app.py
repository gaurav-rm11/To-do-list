from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(100), nullable=False)

    def  __repr__(self):
        return f'<Task {self.sno}-{self.task}>'
@app.route('/', methods = [ 'GET','POST'])
def hello_world():
    if request.method == 'POST':
        task =request.form['to do']
        desc = request.form['desc']
        todo = Todo(task=task, desc=desc)
        db.session.add(todo)
        db.session.commit()
    alldata= Todo.query.all()
    # print(alldata)
    return render_template('index.html', alldata= alldata)
    
@app.route('/delete/<int:sno>')
def delete(sno):
    tasktodelete = Todo.query.filter_by(sno=sno).first()

    if tasktodelete:
        db.session.delete(tasktodelete)
        db.session.commit()

    return redirect("/")



@app.route('/show')
def show():
    alldata= Todo.query.all()
    print(alldata)
    return 'products'

@app.route('/products')
def products():
    return 'products'

if __name__ == "__main__":
    app.run(debug=True, port=8000)