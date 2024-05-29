from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente(db.Model):
    id_cliente = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    morada = db.Column(db.String(255))
    telefone = db.Column(db.String(20), nullable=False)

class Hamburguer(db.Model):
    nome_hamburguer = db.Column(db.String(100), primary_key=True)
    ingredientes = db.Column(db.Text, nullable=False)

class Pedido(db.Model):
    id_pedido = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id_cliente'), nullable=False)
    nome_hamburguer = db.Column(db.String(100), db.ForeignKey('hamburgueres.nome_hamburguer'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    tamanho = db.Column(db.Enum('infantil', 'normal', 'duplo'), nullable=False)
    data_hora = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    valor_total = db.Column(db.Numeric(10, 2), nullable=False)

def init_app(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()