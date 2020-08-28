import unittest
import os
import json

from app import app, db

TEST_DB = 'test.db'


class BasicTestCase(unittest.TestCase):

	def test_index(self):
		"""initial test. ensure flask was set up correctly"""
		tester = app.test_client(self)
		response = tester.get('/', content_type='html/text')
		self.assertEqual(response.status_code, 200)
		
	def test_database(self):
		"""initial test. ensure that the database exists"""
		tester = os.path.exists('app.db')
		self.assertTrue(tester)


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        """Set up a blank temp database before each test"""
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(basedir, TEST_DB)
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        """Destroy blank temp database after each test"""
        db.drop_all()


    def test_empty_db(self):
        """Ensure database is blank."""
        rv = self.app.get('/')
        assert b'No entries yet. Add some!' in rv.data


if __name__=='__main__':
	unittest.main()