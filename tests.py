from project import app, db
from project.models import User, BlogPost
from flask.ext.testing import TestCase
from flask.ext.login import current_user
import unittest

# obvezno Base test Case obvezne funkcije
class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    # povezava z bazo podatkov

    def setUp(self):
        db.create_all()
        db.session.add(BlogPost('Test post', 'To je post namenjen testiranju',2))
        db.session.add(User('admin','admin@app.com', 'student15'))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class FlaskTestCase(BaseTestCase):
    def test_index(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertTrue('Priavi se!' in response.data)

    # posts are on main
    def test_data_displayed(self):
        response = self.client.post('/login', data=dict(username='admin', password='student15'), follow_redirects=True)
        self.assertIn(b'Test', response.data)


class UsersViewsTests(BaseTestCase):

    # correct credentials
    def test_correct_login(self):
        with self.client:
            response = self.client.post('/login', data=dict(username='admin', password='student15'), follow_redirects=True)
            self.assertIn(b'You were just logged in :)', response.data)
            self.assertTrue(current_user.name == 'admin')
            self.assertTrue(current_user.is_active())

    # incorrect credentials
    def test_false_credentials(self):
        response = self.client.post('/login', data=dict(username='burek', password='admin'), follow_redirects=True)
        self.assertIn(b'Invalid credentials! Please try ageain', response.data)

    # logout test
    def test_logout(self):
        with self.client:
            self.client.post('/login', data=dict(username='admin', password='student15'), follow_redirects=True)
            response = self.client.get('/logout', follow_redirects=True)
            self.assertIn(b'You were just logged out :', response.data)


    # login required on main page
    def test_login_required(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertTrue('Please log in to access this page.' in response.data)





if __name__ == '__main__':
    unittest.main()