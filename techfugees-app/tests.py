from datetime import datetime, timedelta
import unittest
from techfugees import app, db
from techfugees.models import User, Post
import techfugees.users.forms

class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_dummy(self):
        assert(True)

if __name__ == '__main__':
    unittest.main(verbosity=2)