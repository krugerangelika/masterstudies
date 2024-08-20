from dash import html
import dash_bootstrap_components as dbc
from app.database import SessionLocal, Patient

class PatientList:
    def __init__(self):
        self.db = SessionLocal()

    def get_all_patients(self):
        patients = self.db.query(Patient).all()
        return patients

    def create_patient_list_layout(self):
        patients = self.get_all_patients()
        if not patients:
            return html.Div("Brak zarejestrowanych pacjentów.")

        return dbc.Container([
            html.H2("Lista Pacjentów"),
            html.Div([
                dbc.Card(
                    dbc.CardBody([
                        html.H4(f"{patient.full_name}, {patient.birthdate}", className="card-title"),
                        html.P(f"Oddział: {patient.department}", className="card-text"),
                        html.P(f"Telefon: {patient.phone}", className="card-text"),
                        html.P(f"Email: {patient.email}", className="card-text"),
                        dbc.Button("Zobacz szczegóły", href=f"/main-panel/patient-details/{patient.id}", color="primary")
                    ])
                ) for patient in patients
            ])
        ], className="mt-5")

    def close_session(self):
        self.db.close()
