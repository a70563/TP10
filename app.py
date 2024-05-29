import sqlite3
from flask import Flask, request, jsonify
from models import db, Cliente, Hamburguer, Pedido, init_app
import json

app = Flask(__name__)
DATABASE = "callcenter.db"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///callcenter.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
init_app(app)


def validar_json(json_string, required_keys) -> bool:
    try:
        # Transforma o JSON string em um dicionário
        data = json.loads(json_string)
    except:  # noqa: E722
        return False

    # Verifica se todas as chaves necessárias estão presentes
    for key in required_keys:
        if key not in data:
            return False

    return True

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/clientes', methods=['GET'])
def get_clientes():
    clientes = Cliente.query.all()
    resultado = [
        {
            "id_cliente": cliente.id_cliente,
            "nome": cliente.nome,
            "morada": cliente.morada,
            "telefone": cliente.telefone
        } for cliente in clientes
    ]
    return jsonify(resultado), 200


@app.route('/clientes', methods=['POST'])
def add_cliente():
    data = request.get_json()
    novo_cliente = Cliente(nome=data['nome'], morada=data.get('morada'), telefone=data['telefone'])
    db.session.add(novo_cliente)
    db.session.commit()
    return jsonify({"message": "Cliente adicionado com sucesso"}), 201


@app.route('/hamburgueres', methods=['GET'])
def get_hamburgueres():
    hamburgueres = Hamburguer.query.all()
    resultado = [
        {
            "nome_hamburguer": hamburguer.nome_hamburguer,
            "ingredientes": hamburguer.ingredientes
        } for hamburguer in hamburgueres
    ]
    return jsonify(resultado), 200


@app.route('/hamburgueres', methods=['POST'])
def add_hamburguer():
    data = request.get_json()
    novo_hamburguer = Hamburguer(nome_hamburguer=data['nome_hamburguer'], ingredientes=data['ingredientes'])
    db.session.add(novo_hamburguer)
    db.session.commit()
    return jsonify({"message": "Hamburguer adicionado com sucesso"}), 201


@app.route('/pedidos', methods=['GET'])
def get_pedidos():
    pedidos = Pedido.query.all()
    resultado = [
        {
            'id_pedido': pedido.id_pedido,
            'id_cliente': pedido.id_cliente,
            'nome_hamburguer': pedido.nome_hamburguer,
            'quantidade': pedido.quantidade,
            'tamanho': pedido.tamanho,
            'data_hora': pedido.data_hora,
            'valor_total': pedido.valor_total
        } for pedido in pedidos
    ]
    return jsonify(resultado), 200


@app.route('/pedidos', methods=['POST'])
def add_pedido():
    data = request.get_json()
    novo_pedido = Pedido(
        id_cliente=data['id_cliente'],
        nome_hamburguer=data['nome_hamburguer'],
        quantidade=data['quantidade'],
        tamanho=data['tamanho'],
        valor_total=data['valor_total']
    )
    db.session.add(novo_pedido)
    db.session.commit()
    return jsonify({"message": "Pedido adicionado com sucesso"}), 201


if __name__ == '__main__':
    app.run(debug=True)

