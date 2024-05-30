import sqlite3

class Database:
    def __init__(self, db_name='call_center.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        with self.conn:
            self.conn.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                morada TEXT,
                telefone TEXT NOT NULL
            )
        """)
            
            self.conn.execute("""
            CREATE TABLE IF NOT EXISTS hamburgueres (
                nome_hamburguer TEXT PRIMARY KEY,
                ingredientes TEXT NOT NULL
            );
        """)
            
            self.conn.execute("""
            CREATE TABLE IF NOT EXISTS pedidos (
                id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
                id_cliente INTEGER,
                nome_hamburguer TEXT,
                quantidade INTEGER NOT NULL,
                tamanho TEXT NOT NULL CHECK (tamanho IN ('infantil', 'normal', 'duplo')),
                data_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
                valor_total REAL NOT NULL,
                FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
                FOREIGN KEY (nome_hamburguer) REFERENCES hamburgueres(nome_hamburguer)
            );
        """)



    def add_cliente(self,nome, morada, telefone):   
        with self.conn:
            self.conn.execute("""
            INSERT INTO clientes (nome, morada, telefone)
            VALUES (?, ?, ?)
        """, (nome, morada, telefone))


    def add_hamburguer(self,nome_hamburguer, ingredientes):
        with self.conn:
            self.conn.execute("""
            INSERT INTO hamburgueres (nome_hamburguer, ingredientes)
            VALUES (?, ?)
        """, (nome_hamburguer, ingredientes))


    def add_pedido(self,id_cliente, nome_hamburguer, quantidade, tamanho, valor_total):
        with self.conn:
            self.conn.execute("""
            INSERT INTO pedidos (id_cliente, nome_hamburguer, quantidade, tamanho, data_hora, valor_total)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (id_cliente, nome_hamburguer, quantidade, tamanho, valor_total))
        
