import json
import unittest

from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db


class CastingTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app)

        self.test_movie = {
            'title': 'Some Movie Title',
            'release_year': 2020
        }

        self.test_actor = {
            'name': 'Jane Doe',
            'age': 22,
            'gender': 'female',
            'movie_id': 1
        }

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.drop_all()
            self.db.create_all()

    def tearDown(self):
        pass

    # GET Endpoint Tests
    # -------------------------------------------------------------------------

    # Creating a test for the /movies GET endpoint
    def test_get_movies(self):
        res = self.client().get('/movies')

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_get_movies_fail(self):
        res = self.client().get('/moovies')

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'Not Found')

    def test_get_actors(self):
        res = self.client().get('/actors')

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_get_actors_fail(self):
        res = self.client().get('/acters')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'Not Found')

    def test_add_movie(self):
        res = self.client().post('/movies/create', json=self.test_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie_id'])

    def test_add_movie_fail(self):
        res = self.client().post(
            '/movies/create',
            json={
                'title': 'Movie Title'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 422)
        self.assertEqual(data['message'], 'unprocessable')

    def test_add_actor(self):
        res = self.client().post('/actors/create', json=self.test_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor_id'])

    def test_add_actor_fail(self):
        res = self.client().post('/actors/create', json={'name': 'John Doe'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 422)
        self.assertEqual(data['message'], 'unprocessable')

    def test_delete_movie(self):
        res = self.client().delete('/movies/delete/2')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])

    def test_delete_movie_fail(self):
        res = self.client().delete('/movies/delete/100000000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'Not Found')

    def test_delete_actor(self):
        res = self.client().delete('/actors/delete/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])

    def test_delete_actor_fail(self):
        res = self.client().delete('/actors/delete/100000000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'Not Found')

    def test_update_movie(self):
        res = self.client().patch(
            '/movies/update/3',
            json={
                'title': 'Updated movie title'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie_id'])

    def test_update_movie_fail(self):
        res = self.client().patch('/movies/update/100000000',
                                  json={'title': 'Updated movie title'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'Not Found')

    def test_update_actor(self):
        res = self.client().patch(
            '/actors/update/2',
            json={
                'name': 'Updated Name'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor_id'])

    def test_update_actor_fail(self):
        res = self.client().patch(
            '/actors/update/100000000',
            json={
                'name': 'Updated Name'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'Not Found')


if __name__ == '__main__':
    unittest.main()
