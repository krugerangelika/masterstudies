import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import random


def generate_mock_drug_data(n=100):
    """
    Generate a list of mock drug data for testing purposes.
    """
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
            'name': random.choice(drug_names),
            'manufacturer': random.choice(manufacturers),
            'description': random.choice(descriptions)
        })

    return data


def create_pharmacy_management_layout():
    """
    Function to create the layout for the pharmacy management section.
    """
    return dbc.Container([
        html.H1("Zarządzanie Lekami i Apteką", className="my-4 text-center"),
        html.Div(id='pharmacy-content')  # Ten element zostanie zaktualizowany
    ], fluid=True)


def create_pharmacy_management(app):
    """
    Function to create a Dash app for pharmacy management.
    """
    dash_app = dash.Dash(__name__, server=app, routes_pathname_prefix='/main-panel/pharmacy-management/',
                         external_stylesheets=[dbc.themes.BOOTSTRAP])

    # Define layout
    dash_app.layout = create_pharmacy_management_layout()

    @dash_app.callback(
        Output('pharmacy-content', 'children'),
        [Input('pharmacy-content', 'id')]
    )
    def render_pharmacy_content(_):
        drug_data = generate_mock_drug_data(100)  # Generuj 100 pozycji z danymi leków

        table_header = [
            html.Thead(html.Tr([html.Th("Nazwa Leku"), html.Th("Producent"), html.Th("Opis")]))
        ]

        table_rows = []
        for drug in drug_data:
            row = html.Tr([
                html.Td(drug['name']),
                html.Td(drug['manufacturer']),
                html.Td(drug['description'])
            ])
            table_rows.append(row)

        table_body = [html.Tbody(table_rows)]

        return dbc.Table(table_header + table_body, bordered=True, hover=True, responsive=True, striped=True)

    return dash_app
