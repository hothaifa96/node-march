# pip install flask

# npm i
# pip install -r requirements.txt

from flask import *

app = Flask(__name__)

@app.route('/welcome',methods=['GET'])
def greet():
    return '<h1> welcome to my site </h1>'

@app.get('/')
def welcome_page():
    return 'hodi'

@app.get('/greet/<name>')
def greet_with_name(name):
    return f'hello  {name}'


@app.get('/sqrt/<int:number>')
def sqrt(number):
    return str(number**0.5)

@app.get('/math/<int:n1>/<sy>/<int:n2>')
def math(n1,sy,n2):
    return f'{n1} {sy} {n2} = {n1*n2 if sy=="*"else n1+n2 if sy == "+" else "naaah" }'




@app.get('/admin')
def admin():
    return 'admin'
@app.get('/user')
def user():
    return 'user'

@app.get('/user/<name>')
def greet_user(name):
    if name in ['ofek','shahar','paz','gil']:
        return redirect(url_for('admin'))
    else:
        return redirect('https://www.youtube.com/watch?v=HlBYdiXdUa8&t=24s&pp=ygUXdGVsbCBtZSB3aHkgYnJvb2tseW4gOTk%3D')

@app.get('/fun')
def fun():
    return render_template('index.html')


@app.post('/login')
def login():
    uname = request.form['uname']
    pword = request.form['pword']

    if uname =='ofek' and pword == '1234':
        return redirect(url_for('admin'))
    else:
        return redirect('https://posterchildprints.com/products/go-fuck-yourself-pose')

app.run()