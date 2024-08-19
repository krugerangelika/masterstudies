import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import numpy as np


def create_dashboard(server):
    app = dash.Dash(server=server, routes_pathname_prefix='/dash/',
                    external_stylesheets=[dbc.themes.BOOTSTRAP])

    # Funkcja do generowania bardziej realistycznego sygnału EKG
    def generate_ecg_waveform(length=400):
        t = np.linspace(0, 1, length)

        # Modelowanie załamków P, QRS, T z odpowiednimi odstępami
        p_wave = 0.1 * np.sin(2 * np.pi * 5 * t) * np.exp(-np.power(t - 0.2, 2) / 0.02)
        q_wave = -0.15 * np.exp(-np.power(t - 0.25, 2) / 0.001)
        r_wave = 1.0 * np.exp(-np.power(t - 0.3, 2) / 0.001)
        s_wave = -0.35 * np.exp(-np.power(t - 0.35, 2) / 0.001)
        t_wave = 0.3 * np.sin(2 * np.pi * 2 * (t - 0.6)) * np.exp(-np.power(t - 0.6, 2) / 0.02)

        # Suma załamków tworzy jeden cykl EKG
        ecg_wave = p_wave + q_wave + r_wave + s_wave + t_wave

        # Powtarzanie sygnału, aby symulować ciągły rytm serca
        ecg_signal = np.tile(ecg_wave, 10)  # Powtórz sygnał, aby stworzyć ciągły sygnał

        return ecg_signal

    # Generowanie sygnału EKG
    ekg_values = generate_ecg_waveform()

    # Przykładowe dane do parametrów życiowych
    heart_rate = np.random.normal(70, 5)
    spo2 = np.random.normal(98, 1)
    systolic = np.random.normal(120, 10)
    diastolic = np.random.normal(80, 5)
    temperature = np.random.normal(36.6, 0.2)

    layout = html.Div([
        # Wyświetlanie wartości numerycznych po lewej stronie
        html.Div([
            html.Div([
                html.H2('HR', style={'color': 'green', 'fontSize': '30px'}),
                html.H1(f"{heart_rate:.0f}", style={'color': 'green', 'fontSize': '50px'}),
            ], style={'textAlign': 'left', 'margin-bottom': '20px'}),
            html.Div([
                html.H2('SpO2', style={'color': 'cyan', 'fontSize': '30px'}),
                html.H1(f"{spo2:.0f}%", style={'color': 'cyan', 'fontSize': '50px'}),
            ], style={'textAlign': 'left', 'margin-bottom': '20px'}),
            html.Div([
                html.H2('Ciśnienie Krwi', style={'color': 'yellow', 'fontSize': '30px'}),
                html.H1(f"{systolic:.0f}/{diastolic:.0f}", style={'color': 'yellow', 'fontSize': '50px'}),
            ], style={'textAlign': 'left', 'margin-bottom': '20px'}),
            html.Div([
                html.H2('Temperatura', style={'color': 'orange', 'fontSize': '30px'}),
                html.H1(f"{temperature:.1f}°C", style={'color': 'orange', 'fontSize': '50px'}),
            ], style={'textAlign': 'left', 'margin-bottom': '20px'}),
        ], style={'flex': '1', 'padding': '20px'}),

        # Wykres EKG po prawej stronie
        html.Div([
            dcc.Graph(
                id='ekg-graph',
                config={'displayModeBar': False}
            ),
        ], style={'flex': '1', 'backgroundColor': 'black', 'padding': '20px', 'margin-bottom': '40px'}),

        dcc.Interval(
            id='interval-component',
            interval=100,  # aktualizacja co 100 ms
            n_intervals=0
        )
    ], style={'display': 'flex', 'backgroundColor': 'black', 'alignItems': 'flex-start'})

    app.layout = html.Div(layout, style={'backgroundColor': 'black'})

    @app.callback(
        Output('ekg-graph', 'figure'),
        Input('interval-component', 'n_intervals')
    )
    def update_ekg(n):
        nonlocal ekg_values

        # Przesuwanie sygnału w lewo, dodając nowe wartości na końcu
        ekg_values = np.roll(ekg_values, -1)

        fig = go.Figure(
            data=[
                go.Scatter(
                    x=np.linspace(0, 1, len(ekg_values)),
                    y=ekg_values,
                    mode='lines',
                    line=dict(color='orange', width=2),
                )
            ],
            layout=go.Layout(
                paper_bgcolor='black',
                plot_bgcolor='black',
                font=dict(color='white', size=15),
                xaxis=dict(showgrid=True, gridcolor='gray', zeroline=False, showticklabels=False),
                yaxis=dict(range=[-1.5, 1.5], showgrid=True, gridcolor='gray', zeroline=False),
                margin=dict(l=10, r=10, t=10, b=10),
            )
        )

        return fig

    return app
