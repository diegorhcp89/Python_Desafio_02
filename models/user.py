from database import db
from flask_login import UserMixin

# Modelo de Usuário
class User(db.Model, UserMixin):
    # Colunas da tabela
    id = db.Column(db.Integer, primary_key=True)  # ID único
    username = db.Column(db.String(80), nullable=False, unique=True)  # Nome de usuário
    password = db.Column(db.String(80), nullable=False)  # Senha (criptografada)
    role = db.Column(db.String(80), nullable=False, default='user')  # Papel do usuário (user/admin)

    def __repr__(self):
        return f"<User {self.username}>"