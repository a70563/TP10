from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'call_center.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/clientes', methods=['GET'])
def get_clientes():
    conn = get_db_connection()
    clientes = conn.execute('SELECT * FROM clientes').fetchall()
    conn.close()
    return jsonify([dict(row) for row in clientes]), 200

@app.route('/clientes', methods=['POST'])
def post_cliente():
    data = request.get_json()
    nome = data['nome']
    morada = data['morada']
    telefone = data['telefone']
    conn = get_db_connection()
    conn.execute('INSERT INTO clientes (nome, morada, telefone) VALUES (?, ?, ?)', (nome, morada, telefone))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Cliente added successfully'}), 201

@app.route('/clientes/<int:cliente_id>', methods=['PUT'])
def put_cliente(cliente_id):
    data = request.get_json()
    nome = data['nome']
    morada = data['morada']
    telefone = data['telefone']
    conn = get_db_connection()
    conn.execute('UPDATE clientes SET nome = ?, morada = ?, telefone = ? WHERE id = ?', (nome, morada, telefone, cliente_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Cliente updated successfully'}), 200

@app.route('/hamburgueres', methods=['GET'])
def get_hamburgueres():
    conn = get_db_connection()
    hamburgueres = conn.execute('SELECT * FROM hamburgueres').fetchall()
    conn.close()
    return jsonify([dict(row) for row in hamburgueres]), 200

@app.route('/hamburgueres', methods=['POST'])
def post_hamburgueres():
    data = request.get_json()
    nome_hamburguer = data['nome_hamburguer']
    ingredientes = data['ingredientes']
    conn = get_db_connection()
    conn.execute('INSERT INTO hamburgueres (nome_hamburguer, ingredientes) VALUES (?, ?)', (nome_hamburguer, ingredientes))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Hambúrguer added successfully'}), 201

@app.route('/hamburgueres/<int:hamburguer_id>', methods=['PUT'])
def put_hamburgueres(hamburguer_id):
    data = request.get_json()
    nome_hamburguer = data['nome_hamburguer']
    ingredientes = data['ingredientes']
    conn = get_db_connection()
    conn.execute('UPDATE hamburgueres SET nome_hamburguer = ?, ingredientes = ? WHERE id = ?', (nome_hamburguer, ingredientes, hamburguer_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Hambúrguer updated successfully'}), 200

@app.route('/pedidos', methods=['GET'])
def get_pedidos():
    conn = get_db_connection()
    pedidos = conn.execute('SELECT * FROM pedidos').fetchall()
    conn.close()
    return jsonify([dict(row) for row in pedidos]), 200

@app.route('/pedidos', methods=['POST'])
def post_pedidos():
    data = request.get_json()
    id_cliente = data['id_cliente']
    nome_hamburguer = data['nome_hamburguer']
    quantidade = data['quantidade']
    tamanho = data['tamanho']
    valor_total = data['valor_total']
    conn = get_db_connection()
    conn.execute('INSERT INTO pedidos (id_cliente, nome_hamburguer, quantidade, tamanho, valor_total) VALUES (?, ?, ?, ?, ?)', (id_cliente, nome_hamburguer, quantidade, tamanho, valor_total))
    conn.commit()
    conn.close()
    return jsonify({'message': 'O seu pedido foi adicionado com sucesso'}), 201

@app.route('/pedidos/<int:pedido_id>', methods=['PUT'])
def put_pedidos(pedido_id):
    data = request.get_json()
    id_cliente = data['id_cliente']
    nome_hamburguer = data['nome_hamburguer']
    quantidade = data['quantidade']
    tamanho = data['tamanho']
    valor_total = data['valor_total']
    conn = get_db_connection()
    conn.execute('UPDATE pedidos SET id_cliente = ?, nome_hamburguer = ?, quantidade = ?, tamanho = ?, valor_total = ? WHERE id_pedido = ?', (id_cliente, nome_hamburguer, quantidade, tamanho, valor_total, pedido_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Pedido atualizado com sucesso'}), 200



if __name__ == '__main__':
    app.run(debug=True)
