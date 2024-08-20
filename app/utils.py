import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Przykładowa baza danych wizyt
VISITS_DATA = []

def create_visit(visit_data):
    """
    Tworzenie nowej wizyty pacjenta
    """
    visit_data['id'] = len(VISITS_DATA) + 1  # Generowanie unikalnego ID wizyty
    VISITS_DATA.append(visit_data)
    return visit_data

def get_visits():
    """
    Pobranie wszystkich wizyt pacjentów
    """
    return VISITS_DATA

def update_visit(visit_id, updated_data):
    """
    Aktualizacja wizyty pacjenta na podstawie ID
    """
    for visit in VISITS_DATA:
        if visit['id'] == visit_id:
            visit.update(updated_data)
            return visit
    return None

def delete_visit(visit_id):
    """
    Usunięcie wizyty pacjenta na podstawie ID
    """
    global VISITS_DATA
    VISITS_DATA = [visit for visit in VISITS_DATA if visit['id'] != visit_id]

# Przykładowe dane pacjentów
PATIENTS_DATA = [
    {
        'id': '1',
        'name': 'Jan Kowalski',
        'age': 45,
        'gender': 'Mężczyzna',
        'room': '101',
        'ward': 'Chirurgiczny',
        'health_status': 'Krytyczny',
        'blood_pressure': '120/80',
        'heart_rate': 75,
        'oxygen_saturation': '98%',
        'admission_date': '2024-08-10',
        'planned_discharge': '2024-08-20',
        'last_update': '2024-08-14 10:00',
        'last_update_by': 'Dr. Nowak',
        'doctor': 'Dr. Nowak'
    },
    {
        'id': '2',
        'name': 'Anna Nowak',
        'age': 33,
        'gender': 'Kobieta',
        'room': '102',
        'ward': 'Kardiologiczny',
        'health_status': 'Stabilny',
        'blood_pressure': '110/70',
        'heart_rate': 70,
        'oxygen_saturation': '99%',
        'admission_date': '2024-08-12',
        'planned_discharge': '2024-08-22',
        'last_update': '2024-08-14 09:00',
        'last_update_by': 'Dr. Kowalski',
        'doctor': 'Dr. Kowalski'
    },
    # Dodaj więcej przykładowych danych pacjentów...
]

def get_patients_data():
    return PATIENTS_DATA

def get_patient_by_id(patient_id):
    for patient in PATIENTS_DATA:
        if patient['id'] == patient_id:
            return patient
    return None

def get_latest_updates():
    # Przykładowe aktualizacje, które można wyświetlać na stronie głównej
    return [
        {
            'title': 'Zmiany w grafiku',
            'content': 'Grafik na najbliższy tydzień został zaktualizowany. Proszę sprawdzić swoje zmiany.',
            'date': datetime.now().strftime('%Y-%m-%d %H:%M')
        },
        {
            'title': 'Nowe procedury',
            'content': 'Od przyszłego tygodnia obowiązują nowe procedury dotyczące higieny na oddziale.',
            'date': datetime.now().strftime('%Y-%m-%d %H:%M')
        },
        {
            'title': 'Aktualizacja stanu pacjentów',
            'content': 'Stan pacjentów na oddziale intensywnej terapii został zaktualizowany. Proszę zapoznać się z raportem.',
            'date': datetime.now().strftime('%Y-%m-%d %H:%M')
        },
    ]

def generate_patient_data(minutes_back=60):
    now = datetime.now()
    start_time = now - timedelta(minutes=minutes_back)
    time_series = pd.date_range(start=start_time, end=now, freq='min')
    num_points = len(time_series)

    return {
        'time': time_series,
        'temperature': np.random.normal(37, 0.5, size=num_points),
        'ekg': np.random.normal(60, 10, size=num_points),
        'heart_rate': np.random.normal(70, 5, size=num_points),
        'oxygen_saturation': np.random.normal(98, 1, size=num_points),
        'blood_pressure_systolic': np.random.normal(120, 10, size=num_points),
        'blood_pressure_diastolic': np.random.normal(80, 5, size=num_points)
    }

def get_patient_data():
    patient_data = {}

    # Sala 1 - Sala 10 - 1 pacjent na salę
    for i in range(1, 11):
        patient_data[f'Sala {i} - Pacjent 1'] = generate_patient_data(minutes_back=60)  # ostatnie 60 minut danych

    return patient_data

# Funkcja uwierzytelniania użytkownika
def authenticate_user(username, password):
    # Przykładowa funkcja uwierzytelniania
    # Zastąp ten kod rzeczywistą logiką uwierzytelniania
    # Możesz połączyć się z bazą danych lub korzystać z API do uwierzytelniania użytkowników
    if username == 'admin' and password == 'password':
        return True

    # utils.py

    VISITS_DATA = []

    def create_visit(patient_id, doctor, date, time, end_time, notes):
        visit = {
            'id': len(VISITS_DATA) + 1,
            'patient_id': patient_id,
            'doctor': doctor,
            'date': date,
            'time': time,
            'end_time': end_time,
            'notes': notes
        }
        VISITS_DATA.append(visit)
        return visit

    def get_visits():
        return VISITS_DATA

    def update_visit(visit_id, doctor, date, time, end_time, notes):
        for visit in VISITS_DATA:
            if visit['id'] == visit_id:
                visit['doctor'] = doctor
                visit['date'] = date
                visit['time'] = time
                visit['end_time'] = end_time
                visit['notes'] = notes
                return visit
        return None

    def delete_visit(visit_id):
        global VISITS_DATA
        VISITS_DATA = [visit for visit in VISITS_DATA if visit['id'] != visit_id]

    return False
