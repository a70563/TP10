import sqlite3

class Database:
    def create_tables():
        conn = sqlite3.connect('call_center.db')
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



            # Criação de clientes
        cursor.execute('''
            INSERT INTO clientes (nome, morada, telefone) VALUES
            ('Joao', 'Rua Eça de Queiroz, 0', '923432234),
            ('Joana', 'Quinta Flor, 19', '923534535')
        ''')

            # Criação de hamburgueres
        cursor.execute('''
            INSERT INTO hamburgueres (nome_hamburguer, ingredientes) VALUES
            ('Hamburguer Super', 'Tomate, alface, queijo'),
            ('Hamburguer Mini', 'Tomate, queijo')
        ''')

            # Inserção de pedidos
        cursor.execute('''
            INSERT INTO pedidos (id_cliente, nome_hamburguer, quantidade, tamanho, data_hora, valor_total) VALUES
            (1, 'Hamburguer Super', 2, 'normal', '2024-02-24 10:31:40', 45.50),
            (2, 'Hamburguer Mini', 1, 'duplo', '2024-09-01 13:12:02', 23.00)
        ''')
            
        conn.commit()
        conn.close()
        
        
