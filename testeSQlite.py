import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect('banco_curso.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS contato(nome, endereco, telefone)")
    cur.execute("INSERT INTO contato VALUES ('Teste 2', '123-456-7890', '555-6789')")
    res = cur.execute("SELECT * FROM contato")
    print(res.fetchall())