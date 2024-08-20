from flask import Flask, render_template, request, redirect, url_for, flash, session
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash
from app.main_panel import create_main_panel
from app.patient_registration import create_patient_registration
from app.patient_visits import create_patient_visits
from app.team_schedule import create_team_schedule
from app.pharmacy_management import create_pharmacy_management
from app.sidebar import register_sidebar_callbacks  # Import funkcji rejestrującej callbacki
from app.database import SessionLocal, User  # Zaktualizowana ścieżka importu

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Stwórz instancje aplikacji Dash dla poszczególnych modułów
main_panel_app = create_main_panel(app)
patient_registration_app = create_patient_registration(app)
patient_visits_app = create_patient_visits(app)
team_schedule_app = create_team_schedule(app)
pharmacy_management_app = create_pharmacy_management(app)

# Zarejestruj callbacki dla sidebaru
register_sidebar_callbacks(main_panel_app)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']

    db = SessionLocal()
    user = db.query(User).filter_by(username=username).first()

    if user and check_password_hash(user.hashed_password, password):
        session['logged_in'] = True
        session['username'] = user.username
        session['position'] = 'Admin' if user.is_admin else 'User'
        flash('Zalogowano pomyślnie!', 'success')
        return redirect('/main-panel/')
    else:
        flash('Błędne dane, zaloguj ponownie!', 'danger')
        return redirect(url_for('login'))

# Funkcja rejestracji nowego użytkownika
@app.route('/register', methods=['POST'])
def register():
    db = SessionLocal()
    username = request.form['new_username']
    email = request.form['new_email']
    full_name = request.form['new_full_name']
    password = request.form['new_password']

    # Sprawdź, czy użytkownik już istnieje
    user = db.query(User).filter((User.username == username) | (User.email == email)).first()
    if user:
        flash('Użytkownik o takiej nazwie użytkownika lub emailu już istnieje!', 'danger')
        return redirect(url_for('login'))

    # Stwórz nowego użytkownika
    hashed_password = generate_password_hash(password)
    new_user = User(
        username=username,
        hashed_password=hashed_password,
        email=email,
        full_name=full_name
    )
    db.add(new_user)
    db.commit()

    flash('Rejestracja przebiegła pomyślnie! Możesz się teraz zalogować.', 'success')
    return redirect(url_for('login'))

# Dodaj aplikacje Dash jako sub-aplikacje
@app.route('/main-panel/')
def main_panel_route():
    return main_panel_app.index()

@app.route('/patient-registration/')
def patient_registration_route():
    return patient_registration_app.index()

@app.route('/main-panel/patient-visits/')
def patient_visits_route():
    return patient_visits_app.index()

@app.route('/main-panel/team-schedule/')
def team_schedule_route():
    return team_schedule_app.index()

@app.route('/main-panel/pharmacy-management/')
def pharmacy_management_route():
    return pharmacy_management_app.index()

if __name__ == '__main__':
    app.run(debug=True)
