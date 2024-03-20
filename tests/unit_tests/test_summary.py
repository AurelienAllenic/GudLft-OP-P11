from server import app

def test_summary_page():
    with app.test_request_context():
        with app.test_client() as client:
            # Connection
            login_response = client.post("/showSummary", data={"email": "john@simplylift.co"})
            assert login_response.status_code == 200
            assert b"Welcome, john@simplylift.co" in login_response.data
            assert b"<title>Summary | GUDLFT Registration</title>" in login_response.data
            assert b"Welcome, john@simplylift.co" in login_response.data

            assert b'<a href="/logout">Logout</a>' in login_response.data

            assert b"Points available:" in login_response.data

            assert b"<h3>Competitions:</h3>" in login_response.data

            assert b"Date:" in login_response.data
            assert b"Number of Places:" in login_response.data
            assert b"Book Places" in login_response.data
