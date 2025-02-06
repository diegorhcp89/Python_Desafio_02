from datetime import datetime
from database import db

# Modelo de Refeição
class Meal(db.Model):
    # Colunas da tabela
    id = db.Column(db.Integer, primary_key=True)  # ID único
    name = db.Column(db.String(80), nullable=False)  # Nome da refeição
    description = db.Column(db.Text, nullable=False)  # Descrição da refeição
    date_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # Data e hora
    in_diet = db.Column(db.Boolean, nullable=False, default=False)  # Está dentro da dieta?
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Relacionamento com o usuário

    def __repr__(self):
        return f"<Meal {self.name}>"