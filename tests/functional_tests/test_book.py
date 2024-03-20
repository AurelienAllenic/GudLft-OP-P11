from server import app
from flask import url_for
from ..utils import load_competitions, load_clubs

def test_book_purchase():
    competitions = load_competitions()
    clubs = load_clubs()
    with app.test_client() as client:
        # Connection
        login_response = client.post("/showSummary", data={"email": "john@simplylift.co"})
        assert login_response.status_code == 200
        assert b"Welcome, john@simplylift.co" in login_response.data

        # GET foreach competition and club
        for comp in competitions:
            for club in clubs:
                book_places_url = url_for('book', competition=comp['name'], club=club['name'])
                book_response = client.get(book_places_url)
                assert book_response.status_code == 200
                assert b"Book" in book_response.data

                num_places = 1
                response = client.post("/purchasePlaces", data={
                    "club": club['name'],
                    "competition": comp['name'],
                    "places": num_places
                })

                assert response.status_code == 200

                # Check for apropriate flash message
                if int(club['points']) < num_places:
                    assert b"Not enough points to make the booking." in response.data
                elif sum(b.get('places', 0) for b in club.get('bookings', []) if b.get('competition') == comp['name']) >= 12:
                    assert b"You can only purchase up to 12 places for the same club in one competition." in response.data
                elif b"Not enough places available in the competition." in response.data:
                    assert b"Not enough places available in the competition." in response.data
                else:
                    assert b"Great-booking complete!" in response.data
