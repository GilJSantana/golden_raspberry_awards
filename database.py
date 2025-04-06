"""Conexão com banco de dados e
 cria as tabelas no SQLite in-memory database.
 Parmetros:
    conn: Conexão com o banco de dados.
    memory: Conexão com o banco de dados em memória.
"""

import sqlite3


def get_connection():
    conn = sqlite3.connect(':memory:')
    conn.row_factory = sqlite3.Row
    return conn


def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            year INTEGER,
            title TEXT,
            studios TEXT,
            winner BOOLEAN
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS producers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movie_producers(
            movie_id INTEGER,
            producer_id INTEGER,
            FOREIGN KEY (movie_id) REFERENCES movies(id),
            FOREIGN KEY (producer_id) REFERENCES producers(id)
        );
    ''')
    conn.commit()
