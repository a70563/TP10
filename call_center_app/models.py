from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente(db.Model):
    id_cliente = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    morada = db.Column(db.String(200))
    telefone = db.Column(db.String(20), nullable=False)

class Hamburguer(db.Model):
    nome_hamburguer = db.Column(db.String(100), primary_key=True)
    ingredientes = db.Column(db.String(200), nullable=False)

class Pedido(db.Model):
    id_pedido = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id_cliente'), nullable=False)
    nome_hamburguer = db.Column(db.String(100), db.ForeignKey('hamburguer.nome_hamburguer'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    tamanho = db.Column(db.String(20), nullable=False)
    data_hora = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    valor_total = db.Column(db.Float, nullable=False)
