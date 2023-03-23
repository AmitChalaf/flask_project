from flask import Flask, render_template, url_for, request, make_response
from forms import StudentForm,get_list,add_student

app = Flask('__name__')

def get_student_list():
    return get_list()

@app.route('/')
def hello():
    return 'hello and welcome'

@app.route('/greet/<name>')
def greet(name):
    return f'hello there {name}'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return f'this is a post request with the values: {username} and {password}'
    
    username = request.args.get('username', 'default value')
    password = request.args.get('password', 'default value')
    return f'this is a get request with the values: {username} and {password}'


@app.route('/grades')
def grades():
    data = request.args
    return render_template('grades.html', data=data)

@app.route('/student',methods=['GET', 'POST'])
def studentform():
    if request.method == 'GET':
        form = StudentForm()
        return render_template('student.html', form = form)

    else:
        form = request.form
        add_student(form)
        list = get_student_list()
        return render_template('studentList.html' ,list = list)

# might be a problem with get_list function
@app.route('/studentList')
def studentList(): 
    list = get_student_list() 
    return render_template('studentList.html', list=list)


if __name__ == "__main__": 
    app.run(debug=True)

