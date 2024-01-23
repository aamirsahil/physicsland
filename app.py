from markupsafe import escape
from flask import Flask, abort, render_template
import datetime

app = Flask(__name__)

def getProblemList(item = None):
    with open('./problems.txt', 'r') as file:
        lines = file.readlines()
    if item==None:
        return lines
    else:
        return lines[item], len(lines)

@app.route('/')
@app.route('/index/')
def home():
    return render_template('index.html', utc_date = datetime.datetime.utcnow().strftime("%H:%M %Y-%m-%d"))

@app.route('/about/')
def about():
    return render_template('about.html', utc_date = datetime.datetime.utcnow().strftime("%H:%M %Y-%m-%d"))

@app.route('/problem/')
def problemList():
    lines = getProblemList()
    return render_template('problemList.html', lines = lines, utc_date = datetime.datetime.utcnow().strftime("%H:%M %Y-%m-%d"))

@app.route('/problem/<problem_num>/')
def problem(problem_num):
    problem_num = escape(problem_num)
    problem_title, total_problem = getProblemList( item=(int(problem_num)-1) )
    return render_template('problem.html',
                            problem_title=problem_title, problem_num=problem_num,
                            total_problem=total_problem,
                            utc_date = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M"))