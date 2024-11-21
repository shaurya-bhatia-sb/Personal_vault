import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this for added security

DATABASE = 'vault.sql'

# Helper function to get the database connection
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Enables dictionary-like cursor behavior
    return conn

# Initialize the database (if needed)
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        );
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS secrets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            secret TEXT NOT NULL
        );
    ''')
    conn.commit()
    conn.close()

# Call the function to initialize the database on app startup
init_db()

# Route for the login page
@app.route('/')
def home():
    return redirect(url_for('login'))

# Route for login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Validate username and password
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()

        if user and check_password_hash(user['password'], password):
            session['username'] = username
            return redirect(url_for('vault'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')

# Route for register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        password_hash = generate_password_hash(password)

        conn = get_db_connection()
        conn.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password_hash))
        conn.commit()
        conn.close()

        return redirect(url_for('login'))

    return render_template('register.html')

# Route for the vault (where secrets are stored)
@app.route('/vault', methods=['GET', 'POST'])
def vault():
    if 'username' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()

    if request.method == 'POST':
        secret = request.form['secret']
        username = session['username']

        # Insert the secret into the database
        conn.execute('INSERT INTO secrets (username, secret) VALUES (?, ?)', (username, secret))
        conn.commit()

    # Retrieve all secrets for the logged-in user
    username = session['username']
    secrets = conn.execute('SELECT * FROM secrets WHERE username = ?', (username,)).fetchall()
    conn.close()

    return render_template('vault.html', secrets=secrets)

# Route for deleting a secret
@app.route('/delete_secret/<int:secret_id>', methods=['POST'])
def delete_secret(secret_id):
    if 'username' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    conn.execute('DELETE FROM secrets WHERE id = ? AND username = ?', (secret_id, session['username']))
    conn.commit()
    conn.close()

    flash('Secret deleted successfully', 'success')
    return redirect(url_for('vault'))

# Route for logout
@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove the username from the session
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
