from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_item():
    response = client.get("/rate?from_currency=usd&to_currency=cad&date=2021-1-1")
    assert response.status_code == 200
    assert response.json() == {"from_currency":"USD","to_currency":"CAD","date":"2021-01-01","exchange_rate":1.274}


def test_read_inexistent_item():
    response = client.get("/rate?from_currency=doesnotexist&to_currency=cad&date=2021-1-1")
    assert response.status_code == 404
    assert response.json()['detail'].startswith('The passed currency ')
    assert response.json()['detail'].endswith(' is not available')


def test_read_item_required_field():
    response = client.get("/rate?")
    assert response.status_code == 422