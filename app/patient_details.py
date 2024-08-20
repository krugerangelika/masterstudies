from dash import html
import dash_bootstrap_components as dbc
from app.database import SessionLocal, Patient

class PatientDetails:
    def __init__(self, patient_id):
        self.db = SessionLocal()
        self.patient_id = patient_id

    def get_patient_details(self):
        patient = self.db.query(Patient).filter(Patient.id == self.patient_id).first()
        return patient

    def create_patient_details_layout(self):
        patient = self.get_patient_details()
        if not patient:
            return html.Div("Pacjent nie został znaleziony.")

        return dbc.Container([
            html.H2(f"Szczegóły pacjenta: {patient.full_name}"),
            html.P(f"Data urodzenia: {patient.birthdate}"),
            html.P(f"Płeć: {patient.gender}"),
            html.P(f"PESEL: {patient.pesel}"),
            html.P(f"Adres: {patient.address}"),
            html.P(f"Telefon: {patient.phone}"),
            html.P(f"Email: {patient.email}"),
            html.P(f"Oddział: {patient.department}"),
            html.P(f"Numer Ubezpieczenia: {patient.insurance_number}"),
            html.P(f"Grupa Krwi: {patient.blood_group}"),
            html.P(f"Rodzaj Dokumentu: {patient.id_type}"),
            html.P(f"Numer Dokumentu: {patient.id_number}"),
            html.P(f"Historia Chorób: {patient.medical_history}"),
            html.P(f"Alergie: {patient.allergies}"),
            dbc.Button("Powrót do listy pacjentów", href="/main-panel/patient-list/", color="secondary")
        ], className="mt-5")

    def close_session(self):
        self.db.close()
