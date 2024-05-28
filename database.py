import sqlite3

# criar uma conexão com o banco de dados
conn = sqlite3.connect('UserData.db')

# criar um cursor para executar comandos sql
cursor = conn.cursor()

# criar a tabela Users se ela não existir
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Email TEXT NOT NULL,
        User TEXT NOT NULL,
        Password TEXT NOT NULL
    );
""")

# inserir um usuario pre-registrado
cursor.execute("""
    INSERT INTO Users (Name, Email, User, Password) VALUES (?, ?, ?, ?)
""", ('manoel', 'manoelferreiramatos.ti@gmail.com', 'admin-manoel', '1234'))

print("Conectado ao Banco de Dados")

conn.commit()