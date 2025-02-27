import pytest
from fastapi.testclient import TestClient
from unittest import mock
from app import app
from models.payment import AddPayment
from dotenv import load_dotenv
from os import getenv


client = TestClient(app)

load_dotenv()


@pytest.fixture
def invalid_payment_data():
    return AddPayment(
        number="7777777777777778",
        expiration_date="01/30",
        cvv="234",
        amount=50000
    )


@pytest.fixture
def valid_payment_data():
    return AddPayment(
        number="7777777777777777",
        expiration_date="01/30",
        cvv="234",
        amount=5000
    )


@pytest.fixture
def success_payment_data():
    return AddPayment(
        number="7777777777777777",
        expiration_date="01/30",
        cvv="234",
        amount=100
    )


def test_add_payment_invalid_credentials(invalid_payment_data):
    with mock.patch('psycopg2.connect'):
        headers = {"Token": getenv("TEST_TOKEN")}
        response = client.post(
            "/api/v1.0/payment/add",
            headers=headers,
            json=invalid_payment_data.model_dump(),
        )
    assert response.status_code == 400
    assert response.json() == {"Message": "Invalid Credencials", "Error": True}


def test_add_payment_not_funds(valid_payment_data):
    with mock.patch('psycopg2.connect'):
        headers = {"Token": getenv("TEST_TOKEN")}
        response = client.post(
            "/api/v1.0/payment/add",
            headers=headers,
            json=valid_payment_data.model_dump(),
        )
    assert response.status_code == 400
    assert response.json() == {"Message": "Insufficient Funds", "Error": True}


def test_add_payment_success(success_payment_data):
    with mock.patch('psycopg2.connect'):
        headers = {"Token": getenv("TEST_TOKEN")}
        response = client.post(
            "/api/v1.0/payment/add",
            json=success_payment_data.model_dump(),
            headers=headers
        )
    assert response.status_code == 200
    assert response.json()["message"] == "Transaccion Exitosa"
    assert response.json()["error"] == False



