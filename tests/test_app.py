import unittest
import os
os.environ['TESTING'] = "true"

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html
        assert "Arshia Zakeri" in html
        assert "about" in html

    def test_timeline_page(self):
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "Add Timeline" in html

    # Test fetching data
    def test_timeline_get(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

    # Test data creation via endpoint
    def test_timeline_post(self):
        example_post = {
            "name": "Batman",
            "email": "bruce@gmail.com",
            "content": "im batman"
        }

        response = self.client.post("/api/timeline_post", data={"name": example_post["name"], "email": example_post["email"], "content": example_post["content"]})
        assert response.status_code == 200
        
