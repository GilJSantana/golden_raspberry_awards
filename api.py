'''
API para o projeto de análise de dados de filmes
Cria os endpoints para acessar os dados processados

Parametros:
    - conn: conexão com o banco de dados
    - intervals: retorna os intervalos de tempo entre os filmes
    - winners: retorna os vencedores de um ano específico
    - studios: retorna o ranking dos estúdios
    - years_with_multiple_winners: retorna os anos com mais de um vencedor

'''

from pathlib import Path

from fastapi import FastAPI, Query

from csv_loader import load_csv_to_db
from database import get_connection, create_tables
from services import (
    get_producer_intervals,
    get_winners_by_year,
    get_studios_ranking,
    get_years_with_multiple_winners
)

base_dir = Path(__file__).resolve().parent
csv_file_path = base_dir / 'dados/Movielist.csv'

app = FastAPI()

conn = get_connection()
create_tables(conn)
load_csv_to_db(conn, csv_file_path)


@app.get("/producers/intervals")
def intervals():
    result = get_producer_intervals(conn)
    return result


@app.get("/winners")
def winners(year: int = Query(..., description="Qual ano deseja? ")):
    result = get_winners_by_year(conn, year)
    return result


@app.get("/studios-ranking")
def studios():
    result = get_studios_ranking(conn)
    return result


@app.get("/years-with-multiple-winners")
def years_with_multiple_winners():
    result = get_years_with_multiple_winners(conn)
    return result
