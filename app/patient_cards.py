from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
from app.database import SessionLocal, Patient

class PatientCards:
    def __init__(self):
        self.db = SessionLocal()

    # Metoda zamykająca sesję
    def close_session(self):
        self.db.close()

    def get_all_patients(self):
        patients = self.db.query(Patient).all()
        return patients

    def create_patient_cards_layout(self):
        patients = self.get_all_patients()
        if not patients:
            return html.Div("Brak zarejestrowanych pacjentów.")

        return dbc.Container([
            html.H2("Karty Pacjentów"),
            html.Div([
                dbc.Card(
                    dbc.CardBody([
                        html.H4(f"{patient.full_name}", className="card-title"),
                        html.P(f"Data urodzenia: {patient.birthdate}", className="card-text"),
                        html.P(f"Oddział: {patient.department}", className="card-text"),
                        html.P(f"Telefon: {patient.phone}", className="card-text"),
                        html.P(f"Email: {patient.email}", className="card-text"),
                        dbc.Button("Zobacz szczegóły", href=f"/main-panel/patient-details/{patient.id}",
                                   color="primary", className="me-2"),
                        dbc.Button("Edytuj", href=f"/main-panel/patient-edit/{patient.id}", color="secondary")
                    ])
                ) for patient in patients
            ])
        ], className="mt-5")

    def create_patient_edit_layout(self, patient_id):
        patient = self.db.query(Patient).filter(Patient.id == patient_id).first()

        if not patient:
            return html.Div("Pacjent nie został znaleziony.")

        return dbc.Container([
            html.H2("Edytuj Dane Pacjenta"),
            dbc.Form([
                dbc.Row([
                    dbc.Col(dbc.Label("Imię i Nazwisko")),
                    dbc.Col(dbc.Input(id="input-name", type="text", value=patient.full_name)),
                ], className="mb-3"),
                dbc.Row([
                    dbc.Col(dbc.Label("Data Urodzenia")),
                    dbc.Col(dbc.Input(id="input-birthdate", type="date", value=patient.birthdate)),
                ], className="mb-3"),
                dbc.Row([
                    dbc.Col(dbc.Label("Płeć")),
                    dbc.Col(dcc.Dropdown(
                        id="input-gender",
                        options=[
                            {"label": "Mężczyzna", "value": "M"},
                            {"label": "Kobieta", "value": "F"}
                        ],
                        value=patient.gender,
                        placeholder="Wybierz płeć"
                    )),
                ], className="mb-3"),
                dbc.Row([
                    dbc.Col(dbc.Label("PESEL")),
                    dbc.Col(dbc.Input(id="input-pesel", type="text", value=patient.pesel)),
                ], className="mb-3"),
                dbc.Row([
                    dbc.Col(dbc.Label("Adres")),
                    dbc.Col(dbc.Input(id="input-address", type="text", value=patient.address)),
                ], className="mb-3"),
                dbc.Row([
                    dbc.Col(dbc.Label("Telefon")),
                    dbc.Col(dbc.Input(id="input-phone", type="text", value=patient.phone)),
                ], className="mb-3"),
                dbc.Row([
                    dbc.Col(dbc.Label("Email")),
                    dbc.Col(dbc.Input(id="input-email", type="email", value=patient.email)),
                ], className="mb-3"),
                dbc.Row([
                    dbc.Col(dbc.Label("Zdjęcie Karty Zdrowia")),
                    dbc.Col(dcc.Upload(
                        id="upload-health-card",
                        children=html.Button('Wybierz plik'),
                        multiple=False
                    )),
                ], className="mb-3"),
                dbc.Row([
                    dbc.Col(dbc.Label("Oddział Szpitalny")),
                    dbc.Col(dcc.Dropdown(
                        id="input-department",
                        options=[
                            {"label": "Anestezjologia i Intensywna Terapii",
                             "value": "Anestezjologia i Intensywna Terapii"},
                            {"label": "Chirurgia Ogólna", "value": "Chirurgia Ogólna"},
                            {"label": "Chirurgia Klatki Piersiowej", "value": "Chirurgia Klatki Piersiowej"},
                            {"label": "Chirurgia Naczyniowa", "value": "Chirurgia Naczyniowa"},
                            {"label": "Chirurgia Onkologiczna", "value": "Chirurgia Onkologiczna"},
                            {"label": "Chirurgia Urazowa", "value": "Chirurgia Urazowa"},
                            {"label": "Dermatologia", "value": "Dermatologia"},
                            {"label": "Ginekologia", "value": "Ginekologia"},
                            {"label": "Ginekologia Onkologiczna", "value": "Ginekologia Onkologiczna"},
                            {"label": "Hematologia", "value": "Hematologia"},
                            {"label": "Internistyczny", "value": "Internistyczny"},
                            {"label": "Kardiologia", "value": "Kardiologia"},
                            {"label": "Kardiologia Interwencyjna", "value": "Kardiologia Interwencyjna"},
                            {"label": "Nefrologii", "value": "Nefrologii"},
                            {"label": "Neurologia", "value": "Neurologia"},
                            {"label": "Neurochirurgia", "value": "Neurochirurgia"},
                            {"label": "Onkologia", "value": "Onkologia"},
                            {"label": "Ortopedia i Traumatologia", "value": "Ortopedia i Traumatologia"},
                            {"label": "Otolaryngologia (Laryngologia)", "value": "Otolaryngologia (Laryngologia)"},
                            {"label": "Pediatria", "value": "Pediatria"},
                            {"label": "Pediatria Onkologiczna", "value": "Pediatria Onkologiczna"},
                            {"label": "Położnictwa", "value": "Położnictwa"},
                            {"label": "Psychiatria", "value": "Psychiatria"},
                            {"label": "Rehabilitacja", "value": "Rehabilitacja"},
                            {"label": "Reumatologia", "value": "Reumatologia"},
                            {"label": "Radiologia", "value": "Radiologia"},
                            {"label": "Urologii", "value": "Urologii"},
                            {"label": "Chirurgia Bariatryczna (Otyłości)",
                             "value": "Chirurgia Bariatryczna (Otyłości)"},
                            {"label": "Medycyna Paliatywna", "value": "Medycyna Paliatywna"},
                            {"label": "Medycyna Ratunkowa", "value": "Medycyna Ratunkowa"},
                            {"label": "Zakaźny", "value": "Zakaźny"},
                            {"label": "Patologia Noworodka", "value": "Patologia Noworodka"},
                            {"label": "Endokrynologia", "value": "Endokrynologia"},
                            {"label": "Medycyna Sportowa", "value": "Medycyna Sportowa"},
                            {"label": "Medycyna Snu", "value": "Medycyna Snu"}
                        ],
                        value=patient.department,
                        placeholder="Wybierz oddział"
                    )),
                ], className="mb-3"),
                dbc.Row([
                    dbc.Col(dbc.Label("Numer Ubezpieczenia Zdrowotnego")),
                    dbc.Col(dbc.Input(id="input-insurance-number", type="text", value=patient.insurance_number)),
                ], className="mb-3"),
                dbc.Row([
                    dbc.Col(dbc.Label("Grupa Krwi")),
                    dbc.Col(dcc.Dropdown(
                        id="input-blood-group",
                        options=[
                            {"label": "A+", "value": "A+"},
                            {"label": "A-", "value": "A-"},
                            {"label": "B+", "value": "B+"},
                            {"label": "B-", "value": "B-"},
                            {"label": "AB+", "value": "AB+"},
                            {"label": "AB-", "value": "AB-"},
                            {"label": "O+", "value": "O+"},
                            {"label": "O-", "value": "O-"}
                        ],
                        value=patient.blood_group,
                        placeholder="Wybierz grupę krwi"
                    )),
                ], className="mb-3"),
                dbc.Row([
                    dbc.Col(dbc.Label("Rodzaj Dokumentu Tożsamości")),
                    dbc.Col(dcc.Dropdown(
                        id="input-id-type",
                        options=[
                            {"label": "Dowód Osobisty", "value": "Dowód Osobisty"},
                            {"label": "Paszport", "value": "Paszport"},
                            {"label": "Prawo Jazdy", "value": "Prawo Jazdy"},
                            {"label": "Inny", "value": "Inny"}
                        ],
                        value=patient.id_type,
                        placeholder="Wybierz rodzaj dokumentu"
                    )),
                ], className="mb-3"),
                dbc.Row([
                    dbc.Col(dbc.Label("Numer Dokumentu Tożsamości")),
                    dbc.Col(dbc.Input(id="input-id-number", type="text", value=patient.id_number)),
                ], className="mb-3"),
                dbc.Row([
                    dbc.Col(dbc.Label("Historia Chorób")),
                    dbc.Col(dbc.Textarea(id="input-medical-history", value=patient.medical_history)),
                ], className="mb-3"),
                dbc.Row([
                    dbc.Col(dbc.Label("Alergie")),
                    dbc.Col(dbc.Textarea(id="input-allergies", value=patient.allergies)),
                ], className="mb-3"),
                dbc.Row([
                    dbc.Col(dbc.Button("Zapisz zmiany", id="save-button", color="primary", n_clicks=0)),
                    dbc.Col(dbc.Button("Powrót do Panelu Głównego", href="/main-panel/", color="secondary", n_clicks=0,
                                       className="me-2")),
                ], justify="end"),
                html.Div(id="output-state", className="mt-3")
            ], className="mt-5"),
        ], className="mt-5")

    @callback(
        [Output('output-state', 'children'),
         Output('input-name', 'value'),
         Output('input-birthdate', 'value'),
         Output('input-gender', 'value'),
         Output('input-pesel', 'value'),
         Output('input-address', 'value'),
         Output('input-phone', 'value'),
         Output('input-email', 'value'),
         Output('input-department', 'value'),
         Output('input-insurance-number', 'value'),
         Output('input-blood-group', 'value'),
         Output('input-id-type', 'value'),
         Output('input-id-number', 'value'),
         Output('input-medical-history', 'value'),
         Output('input-allergies', 'value')],
        Input('save-button', 'n_clicks'),
        State('input-name', 'value'),
        State('input-birthdate', 'value'),
        State('input-gender', 'value'),
        State('input-pesel', 'value'),
        State('input-address', 'value'),
        State('input-phone', 'value'),
        State('input-email', 'value'),
        State('input-department', 'value'),
        State('input-insurance-number', 'value'),
        State('input-blood-group', 'value'),
        State('input-id-type', 'value'),
        State('input-id-number', 'value'),
        State('input-medical-history', 'value'),
        State('input-allergies', 'value'),
        State('url', 'pathname')
    )
    def update_patient(n_clicks, name, birthdate, gender, pesel, address, phone, email, department, insurance_number,
                       blood_group, id_type, id_number, medical_history, allergies, pathname):
        if n_clicks is None or n_clicks == 0:
            return "", name, birthdate, gender, pesel, address, phone, email, department, insurance_number, blood_group, id_type, id_number, medical_history, allergies

        try:
            if not pathname.startswith('/main-panel/patient-edit/'):
                return "Niepoprawna ścieżka URL.", name, birthdate, gender, pesel, address, phone, email, department, insurance_number, blood_group, id_type, id_number, medical_history, allergies

            patient_id = int(pathname.split('/')[-1])

            db = SessionLocal()
            patient = db.query(Patient).filter_by(id=patient_id).first()

            if not patient:
                return "Pacjent nie został znaleziony.", name, birthdate, gender, pesel, address, phone, email, department, insurance_number, blood_group, id_type, id_number, medical_history, allergies

            patient.full_name = name
            patient.birthdate = birthdate
            patient.gender = gender
            patient.pesel = pesel
            patient.address = address
            patient.phone = phone
            patient.email = email
            patient.department = department
            patient.insurance_number = insurance_number
            patient.blood_group = blood_group
            patient.id_type = id_type
            patient.id_number = id_number
            patient.medical_history = medical_history
            patient.allergies = allergies

            db.commit()

            return (
                "Zmiany zostały zapisane!",
                patient.full_name,
                patient.birthdate,
                patient.gender,
                patient.pesel,
                patient.address,
                patient.phone,
                patient.email,
                patient.department,
                patient.insurance_number,
                patient.blood_group,
                patient.id_type,
                patient.id_number,
                patient.medical_history,
                patient.allergies
            )

        except Exception as e:
            return f'Wystąpił błąd: {str(e)}', name, birthdate, gender, pesel, address, phone, email, department, insurance_number, blood_group, id_type, id_number, medical_history, allergies

        finally:
            db.close()
