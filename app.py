from flask import Flask, request, jsonify
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from database import db
import bcrypt
from datetime import datetime
from models.user import User
from models.meal import Meal

# Inicializa o Flask
app = Flask(__name__)

# Configurações do Flask
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/flask-crud'

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

# Rota de login
@app.route('/login', methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        # Busca o usuário no banco de dados
        user = User.query.filter_by(username=username).first()

        # Verifica se o usuário existe e se a senha está correta
        if user and bcrypt.checkpw(str.encode(password), str.encode(user.password)):
            login_user(user)  # Autentica o usuário
            return jsonify({"message": "Autenticação realizada com sucesso"})
    
    return jsonify({"message": "Credenciais inválidas"}), 400

# Rota de logout
@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()  # Desautentica o usuário
    return jsonify({"message": "Logout realizado com sucesso!"})

# Rota para registrar uma refeição
@app.route('/meal', methods=["POST"])
@login_required
def create_meal():
    data = request.json
    name = data.get("name")
    description = data.get("description")
    date_time = data.get("date_time")  # Formato esperado: "YYYY-MM-DD HH:MM:SS"
    in_diet = data.get("in_diet")

    if name and description and date_time and in_diet is not None:
        try:
            date_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return jsonify({"message": "Formato de data inválido. Use 'YYYY-MM-DD HH:MM:SS'"}), 400

        # Cria uma nova refeição
        meal = Meal(
            name=name,
            description=description,
            date_time=date_time,
            in_diet=in_diet,
            user_id=current_user.id  # Associa a refeição ao usuário autenticado
        )
        db.session.add(meal)
        db.session.commit()
        return jsonify({"message": "Refeição registrada com sucesso"}), 201

    return jsonify({"message": "Dados inválidos"}), 400

# Rota para listar todas as refeições do usuário
@app.route('/meals', methods=["GET"])
@login_required
def list_meals():
    meals = Meal.query.filter_by(user_id=current_user.id).all()
    meals_list = []
    for meal in meals:
        meals_list.append({
            "id": meal.id,
            "name": meal.name,
            "description": meal.description,
            "date_time": meal.date_time.strftime("%Y-%m-%d %H:%M:%S"),
            "in_diet": meal.in_diet
        })
    return jsonify(meals_list)

# Rota para atualizar uma refeição
@app.route('/meal/<int:id_meal>', methods=["PUT"])
@login_required
def update_meal(id_meal):
    meal = Meal.query.get(id_meal)

    # Verifica se a refeição existe e pertence ao usuário autenticado
    if not meal or meal.user_id != current_user.id:
        return jsonify({"message": "Refeição não encontrada ou não pertence ao usuário"}), 404

    data = request.json
    name = data.get("name")
    description = data.get("description")
    date_time = data.get("date_time")
    in_diet = data.get("in_diet")

    # Atualiza os campos fornecidos
    if name:
        meal.name = name
    if description:
        meal.description = description
    if date_time:
        try:
            meal.date_time = datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return jsonify({"message": "Formato de data inválido. Use 'YYYY-MM-DD HH:MM:SS'"}), 400
    if in_diet is not None:
        meal.in_diet = in_diet

    db.session.commit()
    return jsonify({"message": "Refeição atualizada com sucesso"})

# Rota para deletar uma refeição
@app.route('/meal/<int:id_meal>', methods=["DELETE"])
@login_required
def delete_meal(id_meal):
    meal = Meal.query.get(id_meal)

    # Verifica se a refeição existe e pertence ao usuário autenticado
    if not meal or meal.user_id != current_user.id:
        return jsonify({"message": "Refeição não encontrada ou não pertence ao usuário"}), 404

    db.session.delete(meal)
    db.session.commit()
    return jsonify({"message": "Refeição deletada com sucesso"})

# Inicia o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)