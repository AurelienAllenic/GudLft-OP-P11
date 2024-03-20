import pytest
from flask import Flask
import sys
sys.path.append("..")


@pytest.fixture
def app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "Welcome to the GUDLFT Registration Portal!"
    return app


@pytest.fixture
def test_client_fixture(app):
    with app.test_client() as client:
        yield client


@pytest.fixture
def competitions():
    return [
        {
            "name": "Spring Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13"
        }
    ]


@pytest.fixture
def clubs():
    return [
        {
            "name": "Simply Lift",
            "email": "john@simplylift.co",
            "points": "13",
            "bookings":[]
        },
        {
            "name": "Iron Temple",
            "email": "admin@irontemple.com",
            "points": "4",
            "bookings":[]
        },
        {
            "name": "She Lifts",
            "email": "kate@shelifts.co.uk",
            "points": "12",
            "bookings":[]
        }
    ]


def get_test_data():
    return {
        "clubs": clubs(),
        "competitions": competitions()
    }
