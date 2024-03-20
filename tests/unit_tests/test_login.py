from server import app

def test_valid_login():
    with app.test_client() as client:
        response = client.post("/showSummary", data={"email": "john@simplylift.co"})
        assert response.status_code == 200
        assert f"Welcome, john@simplylift.co" in str(response.data)


def test_invalid_login():
    with app.test_client() as client:
        response = client.post("/showSummary", data={"email": "invalid@gmail.com"})
        assert response.status_code == 500
