from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy user data
users = {'admin': 'password'}

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', student={'name': 'P. Lakshmi Prasanna'})
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users[username] = password  # Simple in-memory user storage
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return 'Invalid credentials, try again!'
    return render_template('login.html')

@app.route('/resume')
def resume():
    if 'username' in session:
        return render_template('resume.html')
    return redirect(url_for('login'))

@app.route('/projects')
def projects():
    if 'username' in session:
        return render_template('projects.html', student={'name': 'P. Lakshmi Prasanna', 'department': 'CSE'})
    return redirect(url_for('login'))

@app.route('/exit')
def exit_page():
    session.pop('username', None)
    return render_template('exit.html')

if __name__ == '__main__':
    app.run(debug=True)
