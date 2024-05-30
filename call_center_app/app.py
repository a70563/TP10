from flask import Flask, request, jsonify, render_template
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

@app.route('/hamburgueres', methods=['GET'])
def get_hamburgueres():
    conn = get_db_connection()
    hamburgueres = conn.execute('SELECT * FROM hamburgueres').fetchall()
    conn.close()
    return jsonify([dict(row) for row in hamburgueres]), 200

@app.route('/hamburgueres', methods=['POST'])
def post_hamburguer():
    data = request.get_json()
    nome_hamburguer = data['nome_hamburguer']
    ingredientes = data['ingredientes']
    conn = get_db_connection()
    conn.execute('INSERT INTO hamburgueres (nome_hamburguer, ingredientes) VALUES (?, ?)', (nome_hamburguer, ingredientes))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Hambúrguer added successfully'}), 201

@app.route('/pedidos', methods=['GET'])
def get_pedidos():
    conn = get_db_connection()
    pedidos = conn.execute('SELECT * FROM pedidos').fetchall()
    conn.close()
    return jsonify([dict(row) for row in pedidos]), 200

@app.route('/pedidos', methods=['POST'])
def post_pedido():
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
    return jsonify({'message': 'Pedido added successfully'}), 201

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pedidos")
    pedidos = cursor.fetchall()
    conn.close()
    return render_template("pedidos.html", pedidos=pedidos)

if __name__ == '__main__':
    app.run(debug=True)
