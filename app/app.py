from flask import Flask, render_template, request, redirect, url_for, flash, session
from app.main_panel import create_main_panel
from app.patient_registration import create_patient_registration

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Stwórz instancje aplikacji Dash dla poszczególnych modułów
main_panel_app = create_main_panel(app)
patient_registration_app = create_patient_registration(app)

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
app.index = main_panel_app.index
app.patient_registration = patient_registration_app.index

# Wykorzystaj routing Flask do przekazywania zapytań do aplikacji Dash
@app.route('/main-panel/')
def main_panel_route():
    return main_panel_app.index()

@app.route('/main-panel/patient-registration/')
def patient_registration_route():
    return patient_registration_app.index()

# Dodanie obsługi statycznych plików z Reacta
@app.route('/react-components/')
def react_components():
    return render_template('react_index.html')  # Zmień na odpowiedni szablon

# Punkt startowy aplikacji
if __name__ == '__main__':
    app.run(debug=True)
