'''
Carrega os dados do arquivo CSV para o banco de dados SQLite.
Parametros:
    conn: Conexão com o banco de dados.
    csv_file_path: Caminho do arquivo CSV.
'''

import csv
import re



def split_producers(raw_producers_str):
    producers = [producer.strip() for producer in
                 re.split(r',\s*|\s+and\s+', raw_producers_str) if
                 producer.strip()]
    return producers


def load_csv_to_db(conn, csv_file_path):
    cursor = conn.cursor()

    with open(csv_file_path, mode='r', encoding='utf-8',
              newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

        for row in reader:
            year = int(row['year'])
            title = row['title'].strip()
            studios = row['studios'].strip()
            producers_raw = row['producers'].strip()
            winner = row['winner'].strip().lower() == 'yes'

            cursor.execute('''
           INSERT INTO movies (year, title, studios, winner)
           VALUES (?, ?, ?, ?)
           ''', (year, title, studios, winner))
            movie_id = cursor.lastrowid

            producers = split_producers(producers_raw)
            for producer_name in producers:
                cursor.execute('SELECT id FROM producers WHERE name = ?',
                               (producer_name,))
                result = cursor.fetchone()
                if result:
                    producer_id = result['id']
                else:
                    cursor.execute('''
                    INSERT INTO producers (name)
                    VALUES (?)
                    ''', (producer_name,))
                    producer_id = cursor.lastrowid
                cursor.execute('''
                INSERT INTO movie_producers (movie_id, producer_id)
                VALUES (?, ?)''', (movie_id, producer_id))

    conn.commit()
