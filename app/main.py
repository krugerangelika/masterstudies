from database import SessionLocal, User
from sqlalchemy.orm import Session

# Funkcja dodająca nowego użytkownika
def create_user(db: Session, username: str, password: str, email: str, full_name: str = None):
    user = User(
        username=username,
        hashed_password=password,  # W rzeczywistości hasło powinno być hashowane
        email=email,
        full_name=full_name
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Tworzenie sesji i dodawanie użytkownika
db = SessionLocal()

new_user = create_user(
    db=db,
    username="admin",
    password="P@ssw0rd123!",  # Pamiętaj o hashowaniu hasła w prawdziwej aplikacji
    email="admin@example.com",
    full_name="Admin User"
)

print(f"Użytkownik {new_user.username} został utworzony.")
