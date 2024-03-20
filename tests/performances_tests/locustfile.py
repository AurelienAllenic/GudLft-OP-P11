from locust import HttpUser, between, task
import sys
sys.path.append("..")
from utils import load_clubs, load_competitions

class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    competition = load_competitions()[0]
    club = load_clubs()[0]

    @task
    def index_page(self):
        self.client.get("/", name=".index")

    @task
    def points_page(self):
        self.client.get("/points", name='points')
    
    @task
    def show_summary(self):
        data = {'email': 'john@simplylift.co'}
        self.client.post("/showSummary", data=data, name='show_summary')

    @task
    def book_page(self):
        competition = 'Spring Festival'
        club = 'Simply Lift'
        url = '/book/{}/{}'.format(competition, club)
        self.client.get(url, name='book_page')

    @task
    def logout_page(self):
        self.client.get("/logout", name='logout')

    @task
    def purchase_places(self):
        data = {
            'club': 'john@simplylift.co',
            'competition': 'Spring Festival',
            'places': '3'
        }
        self.client.post("/purchasePlaces", data=data, name='purchase_places')
