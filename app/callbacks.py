from dash import Input, Output, State, ctx
from flask import session
from app import app
from app.utils import authenticate_user, send_sms_reminder, send_email_reminder, export_to_google_calendar

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

@app.callback(
    Output('med-registration-feedback', 'children'),
    Input('register-med-button', 'n_clicks'),
    [State('input-med-name', 'value'),
     State('input-med-quantity', 'value'),
     State('input-med-expiry', 'value'),
     State('input-med-price', 'value')]
)
def register_medication(n_clicks, name, quantity, expiry, price):
    if n_clicks:
        if not name or not quantity or not expiry or not price:
            return "Proszę wypełnić wszystkie wymagane pola."

        # Logika zapisywania leku
        # Tutaj dodaj kod do zapisania leku w bazie danych lub w pamięci aplikacji

        return f"Lek {name} został pomyślnie zarejestrowany."
    return ""

@app.callback(
    Output('orders-history', 'children'),
    Input('view-orders-button', 'n_clicks'),
    [State('input-order-number', 'value'),
     State('input-order-date', 'value'),
     State('input-order-status', 'value')]
)
def view_orders(n_clicks, order_number, order_date, order_status):
    if n_clicks:
        # Logika przeglądania zamówień
        # Tutaj dodaj kod do przetwarzania i wyświetlania zamówień

        return f"Wyświetlane są zamówienia: {order_number}, {order_date}, {order_status}."
    return ""
