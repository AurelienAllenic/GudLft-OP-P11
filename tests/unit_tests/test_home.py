from server import app

def test_index():
    """Test the index route."""
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert b"Welcome to the GUDLFT Registration Portal!" in response.data
