import sqlite3



def create_tables():
        conn = sqlite3.connect('callcenter.db')
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                morada TEXT,
                telefone TEXT NOT NULL
            )
        """)
            
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS hamburgueres (
                nome_hamburguer TEXT PRIMARY KEY,
                ingredientes TEXT NOT NULL
            );
        """)
            
        cursor.execute("""
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
        
        conn.commit()
        conn.close()



def add_cliente(nome, morada, telefone):
        conn = sqlite3.connect('callcenter.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO clientes (nome, morada, telefone)
            VALUES (?, ?, ?)
        """, (nome, morada, telefone))
        conn.commit()
        conn.close()

def add_hamburguer(nome_hamburguer, ingredientes):
        conn = sqlite3.connect('callcenter.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO hamburgueres (nome_hamburguer, ingredientes)
            VALUES (?, ?)
        """, (nome_hamburguer, ingredientes))
        conn.commit()
        conn.close()

def add_pedido(id_cliente, nome_hamburguer, quantidade, tamanho, valor_total):
        conn = sqlite3.connect('callcenter.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO pedidos (id_cliente, nome_hamburguer, quantidade, tamanho, data_hora, valor_total)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (id_cliente, nome_hamburguer, quantidade, tamanho, valor_total))
        conn.commit()
        conn.close()
