from flask import Flask, render_template, request, redirect, url_for, session
import bcrypt
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# Hardcoded user credentials for demonstration purposes
# In a real application, store hashed passwords in a database
users = {
    "admin": bcrypt.hashpw(b"password", bcrypt.gensalt())  # Hash the password
}

@app.route('/')
def home():
    if 'logged_in' in session and session['logged_in']:
        return "Welcome to the Secure Web App!"
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']  # Get the password from the form

        # Check if the username exists and the password is correct
        if username in users and bcrypt.checkpw(password.encode('utf-8'), users[username]):
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            return "Invalid credentials!"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)  # Clear the session
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')  # Enable HTTPS
