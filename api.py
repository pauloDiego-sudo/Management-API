from flask import Flask, request, jsonify #Para web
from sqlalchemy.dialects.postgresql import UUID #Para o dtatatype uuid no DB
from sqlalchemy.exc import IntegrityError #Para tratamento de erros no banco de dados
from flask_sqlalchemy import SQLAlchemy #Para persistencia/banco de dados
from config import DevConfig #Para configuração do banco de dados
from marshmallow import Schema, fields, ValidationError, post_load #Para validação de dados
import validators as vd #Para validação de dados

import uuid

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

# Definição do modelo de Usuário para o DB
class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(100))
    cpf = db.Column(db.String(14),unique=True)  # Assumindo que CPF será armazenado como string e como valores unicos
    age = db.Column(db.String(3))  # Assumindo que idade será armazenada como string

    def __init__(self, name, cpf, age):
        self.name = name
        self.cpf = cpf
        self.age = age

# Definição do schema de Usuário para validação de dados
class UsersSchema(Schema):
    id = fields.UUID(dump_only=True) # dump_only significa que o campo não será considerado na hora de fazer o load
    name = fields.Str()
    cpf = fields.Str(validate=vd.valida_cpf)
    age = fields.Str(validate=vd.valida_idade)

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)

# Endpoint para criar um usuário
@app.route('/users', methods=['POST'])
def create_user():
    schema = UsersSchema()
    data = request.get_json()
    try:
        user = schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 422
    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError as err:
        return jsonify({'message': 'Invalid input'}), 400

    return jsonify({'message': 'User created successfully'}), 201

# Endpoint para obter todos os usuários
@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    schema = UsersSchema(many=True)
    return jsonify(schema.dump(users)), 200

# Endpoint para obter um usuário
@app.route('/users/<string:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        schema = UsersSchema()
        return jsonify(schema.dump(user)), 200
    return jsonify({'message': 'User not found'}), 404

# Endpoint para atualizar um usuário
@app.route('/users/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    original_user = User.query.get(user_id)
    if original_user:
        data = request.get_json()
        schema = UsersSchema()
        try:
            user = schema.load(data)
        except ValidationError as err:
            return jsonify(err.messages), 422
        original_user.name = user.name
        original_user.cpf = user.cpf
        original_user.age = user.age
        db.session.commit()
        return jsonify({'message': 'User updated successfully'}), 200
    return jsonify({'message': 'User not found'}), 404

# Endpoint para deletar um usuário
@app.route('/users/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 200
    return jsonify({'message': 'User not found'}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
