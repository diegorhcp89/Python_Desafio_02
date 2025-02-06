from flask import Flask, request, jsonify
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from database import db
import bcrypt
from datetime import datetime

# Inicializa o Flask
app = Flask(__name__)

# Configurações do Flask
app.config['SECRET_KEY'] = "your_secret_key"  # Chave secreta para sessões
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/flask-crud'  # Conexão com o banco de dados

# Inicializa o SQLAlchemy e o LoginManager
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)

# Define a view de login (para redirecionar usuários não autenticados)
login_manager.login_view = 'login'

# Função para carregar o usuário a partir do ID (necessário para o Flask-Login)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Rota inicial para teste
@app.route("/hello-world", methods=["GET"])
def hello_world():
    return "Hello world"

# Inicia o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)