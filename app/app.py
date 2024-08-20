from flask import Flask, render_template, request, redirect, url_for, flash, session
from app.main_panel import create_main_panel
from app.patient_registration import create_patient_registration
from app.patient_visits import create_patient_visits
from app.team_schedule import create_team_schedule
from app.pharmacy_management import create_pharmacy_management  # Upewnij się, że ta funkcja jest poprawna

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Stwórz instancje aplikacji Dash dla poszczególnych modułów
main_panel_app = create_main_panel(app)
patient_registration_app = create_patient_registration(app)
patient_visits_app = create_patient_visits(app)
team_schedule_app = create_team_schedule(app)
pharmacy_management_app = create_pharmacy_management(app)  # Dodaj zarządzanie apteką

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']

    if username == "admin" and password == "P@ssw0rd123!":
        session['logged_in'] = True
        session['username'] = 'Admin'
        session['position'] = 'Admin'
        flash('Zalogowano pomyślnie!', 'success')
        return redirect('/main-panel/')
    else:
        flash('Błędne dane, zaloguj ponownie!', 'danger')
        return redirect(url_for('login'))

# Dodaj aplikacje Dash jako sub-aplikacje
@app.route('/main-panel/')
def main_panel_route():
    return main_panel_app.index()

@app.route('/main-panel/patient-registration/')
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
