from server import app

def test_logout():
    with app.test_client() as client:
        response = client.post("/showSummary", data={"email": "john@simplylift.co"})
        assert response.status_code == 200
        assert f"Welcome, john@simplylift.co" in str(response.data)

        # Effectuer la requête de déconnexion
        logout_response = client.get("/logout", follow_redirects=True)
        assert logout_response.status_code == 200
