from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, Date, Enum, Text, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Ustawienia połączenia z bazą danych MySQL
DATABASE_URL = "mysql+mysqlconnector://root:Test1234!@localhost/medical_app"

# Tworzenie silnika SQLAlchemy
engine = create_engine(DATABASE_URL)

# Baza dla SQLAlchemy
Base = declarative_base()

# Tworzenie sesji do komunikacji z bazą danych
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Model użytkownika
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    hashed_password = Column(String(128), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    full_name = Column(String(100))
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

# Model pacjenta
class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    birthdate = Column(Date, nullable=False)
    gender = Column(Enum('M', 'F'), nullable=False)
    pesel = Column(String(11), nullable=False, unique=True)
    address = Column(String(255), nullable=False)
    phone = Column(String(15), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    health_card_image_path = Column(String(255))
    department = Column(String(100), nullable=False)
    insurance_number = Column(String(50))
    blood_group = Column(Enum('A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'))
    id_type = Column(Enum('Dowód Osobisty', 'Paszport', 'Prawo Jazdy', 'Inny'))
    id_number = Column(String(50))
    medical_history = Column(Text)
    allergies = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

# Tworzenie tabeli w bazie danych (jeśli jeszcze nie istnieje)
Base.metadata.create_all(bind=engine)
