from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# In-memory user storage (replace this with a database in a real project)
users = []

@app.route('/')
def index():
    return render_template('index.html', users=users)

@app.route('/admin')
def admin():
    return render_template('admin.html', users=users)

@app.route('/create_user', methods=['POST'])
def create_user():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Check if the username is unique
    if any(user['username'] == username for user in users):
        flash('Username already exists', 'danger')
    else:
        users.append({'username': username, 'password': password})
        flash('User created successfully', 'success')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
