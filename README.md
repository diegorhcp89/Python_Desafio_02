# Daily Diet API

A **Daily Diet API** é uma aplicação backend desenvolvida em Python com o framework Flask. Ela permite o gerenciamento de refeições diárias, oferecendo funcionalidades para registrar, editar, listar e deletar refeições, além de autenticação de usuários.

## Funcionalidades

### Autenticação de Usuários
- Registro e login de usuários.
- Controle de acesso baseado em roles (usuário/admin).

### Gerenciamento de Refeições
- Registrar uma refeição com nome, descrição, data/hora e indicação se está dentro da dieta.
- Editar uma refeição existente.
- Deletar uma refeição.
- Listar todas as refeições de um usuário.
- Visualizar detalhes de uma refeição específica.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Flask**: Framework web para desenvolvimento da API.
- **Flask-SQLAlchemy**: Integração com banco de dados.
- **Flask-Login**: Gerenciamento de autenticação de usuários.
- **MySQL**: Banco de dados para armazenamento das informações.
- **Docker**: Containerização do banco de dados MySQL.
- **bcrypt**: Criptografia de senhas.

## Estrutura do Projeto

```
/daily-diet-api
  /models
    - user.py          # Modelo de usuário
    - meal.py          # Modelo de refeição
  - app.py             # Aplicação Flask (rotas e lógica)
  - database.py        # Configuração do SQLAlchemy
  - requirements.txt   # Dependências do projeto
  - docker-compose.yml # Configuração do Docker para o MySQL
  - README.md          # Documentação do projeto
```

## Como Executar o Projeto

### Pré-requisitos

- **Docker**: Para subir o banco de dados MySQL.
- **Python 3.x**: Para executar a aplicação Flask.
- **Pip**: Para instalar as dependências.

### Passos para Execução

#### 1. Subir o Banco de Dados
```bash
docker-compose up -d
```

#### 2. Instalar Dependências
```bash
pip install -r requirements.txt
```

#### 3. Executar a Aplicação
```bash
python app.py
```
A API estará disponível em `http://localhost:5000`.

#### 4. Testar as Rotas
Use ferramentas como **Postman** ou **Insomnia** para testar as rotas da API.

## Rotas da API

### Autenticação

#### **POST /login**
Autentica um usuário.

**Body (JSON):**
```json
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

#### **GET /logout**
Desautentica o usuário atual.

### Refeições

#### **POST /meal**
Registra uma nova refeição.

**Body (JSON):**
```json
{
  "name": "Café da Manhã",
  "description": "Pão integral com ovo e suco de laranja",
  "date_time": "2023-10-01 08:00:00",
  "in_diet": true
}
```

#### **GET /meals**
Lista todas as refeições do usuário autenticado.

#### **PUT /meal/:id_meal**
Atualiza uma refeição existente.

**Body (JSON):**
```json
{
  "name": "Café da Manhã",
  "description": "Pão integral com ovo e suco de laranja",
  "date_time": "2023-10-01 08:30:00",
  "in_diet": false
}
```

#### **DELETE /meal/:id_meal**
Deleta uma refeição existente.

## Exemplo de Uso

#### **1. Fazer login**
```bash
POST /login
Body: { "username": "user1", "password": "senha123" }
```

#### **2. Registrar uma refeição**
```bash
POST /meal
Body: {
  "name": "Almoço",
  "description": "Arroz, feijão e frango grelhado",
  "date_time": "2023-10-01 12:30:00",
  "in_diet": true
}
```

#### **3. Listar as refeições**
```bash
GET /meals
```

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo:

1. Faça um **fork** do projeto.
2. Crie uma **branch** para sua feature:
   ```bash
   git checkout -b feature/nova-feature
   ```
3. Commit suas mudanças:
   ```bash
   git commit -m 'Adiciona nova feature'
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin feature/nova-feature
   ```
5. Abra um **Pull Request**.

