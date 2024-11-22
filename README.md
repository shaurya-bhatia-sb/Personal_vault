# Personal Vault

**Personal Vault** is a secure Flask-based web application designed for storing confidential secrets with user authentication and data management functionality.

## Features

- **User Authentication**:
  - Secure registration and login system using hashed passwords.
  - Logout functionality to secure sessions.

- **Secrets Management**:
  - Add, view, and delete secrets in a secure environment.
  - View all previous secrets in a collapsible interface, including timestamps.

- **Database**:
  - SQLite database for storing user credentials and secrets.

## Folder Structure

```
Personal_vault/
├── templates/
│   ├── login.html       # Login page
│   ├── register.html    # Registration page
│   ├── vault1.html      # Vault interface
│   └── base.html        # Shared base template (if applicable)
├── static/
│   ├── styles.css       # CSS for the application
├── app.py               # Main Flask application
├── vault.db             # SQLite database
├── requirements.txt     # Project dependencies
└── README.md            # Documentation
```

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/shaurya-bhatia-sb/Personal_vault.git
   cd Personal_vault
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - **Windows**: `venv\Scripts\activate`
   - **macOS/Linux**: `source venv/bin/activate`

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Initialize the database:
   ```bash
   python app.py
   ```

6. Start the server:
   ```bash
   python app.py
   ```

7. Access the application at:
   ```
   http://127.0.0.1:5000
   ```

## Technologies Used

- **Backend**: Flask
- **Frontend**: HTML, CSS
- **Database**: SQLite

## How It Works

1. **Register/Login**: Securely register or log in to access the vault.
2. **Vault**: Add secrets to your personal vault. View previous secrets with their creation timestamps.
3. **Logout**: Securely end your session.

## Future Enhancements

- Implement password recovery.
- Add multi-user support with role-based permissions.
- Enable data export/import functionality.

## License

This project is licensed under the MIT License. 



