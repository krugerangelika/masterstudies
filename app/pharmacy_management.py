import dash
from dash import dcc, html, callback_context
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, MATCH
import random
from datetime import datetime, timedelta

# Funkcja generująca przykładowe dane o lekach
def generate_mock_drug_data(n=10):
    drug_names = [
        "Aspirin", "Paracetamol", "Ibuprofen", "Amoxicillin", "Metformin",
        "Simvastatin", "Omeprazole", "Losartan", "Gabapentin", "Hydrochlorothiazide"
    ]
    manufacturers = [
        "PharmaCorp", "HealthGen", "MedLife", "BioPharma", "WellCare",
        "MediPro", "GlobalMed", "CarePlus", "BioMedix", "HealthFirst"
    ]
    descriptions = [
        "Stosowany do leczenia bólu i gorączki.",
        "Lek przeciwwirusowy stosowany w leczeniu infekcji.",
        "Przeznaczony do leczenia zapaleń i obrzęków.",
        "Antybiotyk stosowany w leczeniu infekcji bakteryjnych.",
        "Lek stosowany w leczeniu cukrzycy typu 2.",
        "Stosowany do obniżania poziomu cholesterolu.",
        "Lek stosowany w leczeniu refluksu żołądkowego.",
        "Przeznaczony do leczenia nadciśnienia tętniczego.",
        "Lek przeciwbólowy stosowany w neuropatii.",
        "Diuretyk stosowany w leczeniu nadciśnienia."
    ]
    data = []
    for i in range(n):
        data.append({
            'id': i,
            'name': random.choice(drug_names),
            'manufacturer': random.choice(manufacturers),
            'description': random.choice(descriptions),
            'order_date': "",
            'delivery_date': "",
            'status': ""
        })
    return data

# Funkcja tworząca layout zarządzania lekami
def create_pharmacy_management_layout(drug_data):
    table_header = [
        html.Thead(html.Tr([html.Th("Nazwa Leku"), html.Th("Producent"), html.Th("Opis"), html.Th("Akcja"), html.Th("Data zamówienia"), html.Th("Data dostawy"), html.Th("Status zamówienia")]))
    ]

    table_rows = []
    for drug in drug_data:
        row = html.Tr([
            html.Td(drug['name']),
            html.Td(drug['manufacturer']),
            html.Td(drug['description']),
            html.Td(dbc.Button("Zamów z apteki", id={'type': 'order-button', 'index': drug['id']}, color="primary")),
            html.Td(drug['order_date'], id={'type': 'order-date', 'index': drug['id']}),
            html.Td(drug['delivery_date'], id={'type': 'delivery-date', 'index': drug['id']}),
            html.Td(drug['status'], id={'type': 'status', 'index': drug['id']})
        ])
        table_rows.append(row)

    table_body = [html.Tbody(table_rows)]

    return dbc.Container([
        html.H1("Zarządzanie Lekami i Apteką", className="my-4 text-center"),
        dbc.Table(table_header + table_body, bordered=True, hover=True, responsive=True, striped=True)
    ], fluid=True)

# Funkcja tworząca aplikację Dash do zarządzania lekami
def create_pharmacy_management(server):
    dash_app = dash.Dash(__name__, server=server, routes_pathname_prefix='/main-panel/pharmacy-management/',
                         external_stylesheets=[dbc.themes.BOOTSTRAP])

    drug_data = generate_mock_drug_data(10)  # Generowanie danych o lekach
    dash_app.layout = create_pharmacy_management_layout(drug_data)  # Przekazanie danych do layoutu

    @dash_app.callback(
        [Output({'type': 'order-date', 'index': MATCH}, 'children'),
         Output({'type': 'delivery-date', 'index': MATCH}, 'children'),
         Output({'type': 'status', 'index': MATCH}, 'children')],
        [Input({'type': 'order-button', 'index': MATCH}, 'n_clicks')]
    )
    def update_order_status(n_clicks):
        if n_clicks and n_clicks > 0:
            order_date = datetime.now().strftime('%Y-%m-%d %H:%M')
            delivery_date = (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d %H:%M')
            status = "Zamówiono"
            return order_date, delivery_date, status
        return "", "", ""

    return dash_app

