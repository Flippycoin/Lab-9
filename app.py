from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
db = SQLAlchemy(app)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(100), nullable=False)

    def init(self, title, link):
        self.title = title
        self.link = link

@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)

@app.route('/add_project', methods=['POST'])
def add_project():
    title = request.form['title']
    link = request.form['link']
    new_project = Project(title=title, link=link)
    db.session.add(new_project)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    #db.create_all()
    app.run(debug=True)
