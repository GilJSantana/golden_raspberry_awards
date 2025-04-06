from fastapi.testclient import TestClient

from api import app

client = TestClient(app)


def test_get_producers_intervals():
    response = client.get("/producers/intervals")
    assert response.status_code == 200
    data = response.json()
    assert "min" in data and "max" in data


def test_get_winners_by_year():
    response = client.get("/winners?year=1986")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for movie in data:
        assert "title" in movie
        assert "studios" in movie


def test_get_studios_ranking():
    response = client.get("/studios-ranking")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert "studios" in data[0]
    assert "win_count" in data[0]


def test_get_years_with_multiple_winners():
    response = client.get("/years-with-multiple-winners")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for item in data:
        assert "year" in item
        assert "winner_count" in item
