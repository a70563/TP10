import sqlite3

def get_db_connection():
    conn = sqlite3.connect('call_center.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            morada TEXT,
            telefone TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS hamburgueres (
            nome_hamburguer TEXT PRIMARY KEY,
            ingredientes TEXT NOT NULL
        )
    ''')

    cursor.execute('''
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
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
