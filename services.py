'''
Este modulo acessa o banco de dados e fornece funcoes para obter informacoes sobre os vencedores.
Ele possui as seguintes funcoes:
1. get_producer_intervals(conn): Retorna os intervalos entre os anos em que os produtores ganharam.
2. get_winners_by_year(conn, year): Retorna os vencedores de um determinado ano.
3. get_studios_ranking(conn): Retorna a contagem de vitorias por estúdio.
4. get_years_with_multiple_winners(conn): Retorna os anos em que houve mais de um vencedor.

parametros:
conn: Conexao com o banco de dados.

'''

from collections import defaultdict


def get_producer_intervals(conn):
    cursor = conn.cursor()

    cursor.execute('''
                   SELECT p.name, m.year
                     FROM producers p
                     JOIN movie_producers mp ON p.id = mp.producer_id
                     JOIN movies m ON m.id = mp.movie_id
                     WHERE m.winner = 1
                     ORDER BY p.name, m.year
                   ''')

    producer_wins = defaultdict(list)
    for row in cursor.fetchall():
        producer_name, year = row
        producer_wins[producer_name].append(year)

    result = []

    for name, years in producer_wins.items():
        if len(years) < 2:
            continue
        for i in range(1, len(years)):
            interval = years[i] - years[i - 1]
            result.append({
                "producer": name,
                "interval": interval,
                "previousWin": years[i - 1],
                "followingWin": years[i],
            })

    if not result:
        return {"min": [], "max": []}

    min_interval = min(r["interval"] for r in result)
    max_interval = max(r["interval"] for r in result)

    return {
        'min': [r for r in result if r["interval"] == min_interval],
        'max': [r for r in result if r["interval"] == max_interval]
    }


def get_winners_by_year(conn, year):
    cursor = conn.cursor()

    cursor.execute('''
                   SELECT title, studios
                     FROM movies
                     WHERE year = ? AND winner = 1
                   ''', (year,))

    winner_by_year = [{'title': row['title'], 'studios': row['studios']} for
                      row in cursor.fetchall()]
    return winner_by_year


def get_studios_ranking(conn):
    cursor = conn.cursor()

    cursor.execute('''
                   SELECT studios, COUNT(*) as win_count
                     FROM movies
                     WHERE winner = 1
                     GROUP BY studios
                     ORDER BY win_count DESC
                   ''')

    studio_ranking = [
        {'studios': row['studios'], 'win_count': row['win_count']} for
        row in cursor.fetchall()]
    return studio_ranking


def get_years_with_multiple_winners(conn):
    cursor = conn.cursor()

    cursor.execute('''
                   SELECT year, COUNT(*) as total_winners
                     FROM movies
                     WHERE winner = 1
                     GROUP BY year
                     HAVING total_winners > 1
                     ORDER BY year
                   ''')

    years_with_multiple_winners = [
        {'year': row['year'], 'winner_count': row['total_winners']} for row in
        cursor.fetchall()]
    return years_with_multiple_winners
