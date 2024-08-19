from dash import Input, Output, State
from flask import session
from app import app
from app.utils import authenticate_user  # Zakładam, że funkcja jest w utils.py


@app.callback(
    [Output('url_login', 'pathname'),
     Output('login-container', 'style'),
     Output('dashboard-container', 'style'),
     Output('output-state', 'children')],
    [Input('login-button', 'n_clicks'),
     Input('logout-button', 'n_clicks')],
    [State('uname-box', 'value'),
     State('pwd-box', 'value')]
)
def manage_login_logout(login_n_clicks, logout_n_clicks, username, password):
    ctx = dash.callback_context

    login_n_clicks = login_n_clicks or 0
    logout_n_clicks = logout_n_clicks or 0

    if ctx.triggered:
        triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if triggered_id == 'login-button' and login_n_clicks > 0:
            if authenticate_user(username, password):
                session['logged_in'] = True
                return '/main-panel', {'display': 'none'}, {'display': 'block'}, ''
            else:
                return '/login', {'display': 'block'}, {'display': 'none'}, 'Nieprawidłowa nazwa użytkownika lub hasło'

        elif triggered_id == 'logout-button' and logout_n_clicks > 0:
            session['logged_in'] = False
            return '/login', {'display': 'block'}, {'display': 'none'}, ''

    if session.get('logged_in'):
        return '/main-panel', {'display': 'none'}, {'display': 'block'}, ''
    else:
        return '/login', {'display': 'block'}, {'display': 'none'}, ''


# Callback do obsługi formularza rejestracji pacjenta
@app.callback(
    Output('output-state', 'children'),
    Input('submit-button', 'n_clicks'),
    [State('input-name', 'value'),
     State('input-birthdate', 'value'),
     State('input-gender', 'value'),
     State('input-pesel', 'value'),
     State('input-address', 'value'),
     State('input-phone', 'value'),
     State('input-email', 'value'),
     State('upload-health-card', 'contents')]
)
def register_patient(n_clicks, name, birthdate, gender, pesel, address, phone, email, health_card):
    if n_clicks:
        # Przykładowa logika rejestracji pacjenta - tutaj można dodać zapisywanie do bazy danych
        if not name or not birthdate or not pesel or not phone:
            return "Proszę wypełnić wszystkie wymagane pola."

        # Weryfikacja numeru PESEL (przykład)
        if len(pesel) != 11 or not pesel.isdigit():
            return "Nieprawidłowy numer PESEL."

        # Zapisz dane pacjenta do bazy danych (tutaj przykładowo w session)
        session['last_registered_patient'] = {
            'name': name,
            'birthdate': birthdate,
            'gender': gender,
            'pesel': pesel,
            'address': address,
            'phone': phone,
            'email': email,
            'health_card': health_card
        }

        return f"Pacjent {name} został pomyślnie zarejestrowany."

    return ""  # Zwróć pusty ciąg jeśli przycisk nie został jeszcze kliknięty
