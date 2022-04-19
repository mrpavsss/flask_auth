"""Testing db stuffs"""
from faker import Faker
from app import db
from app.db.models import User, Song

def test_adding_user(application):
    """test to see new user"""
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0
        user = User('pr253@njit.edu', 'testtest')
        db.session.add(user)
        db.session.commit()
        assert db.session.query(User).count() == 1
        user = User.query.filter_by(email='pr253@njit.edu').first()
        assert user.email == 'pr253@njit.edu'
        user.songs= [Song("test")]
        db.session.commit()
        assert db.session.query(Song).count() == 1
        song1 = Song.query.filter_by(title='test').first()
        assert song1.title == "test"
        song1.title = "spam"
        db.session.commit()
        song2 = Song.query.filter_by(title='spam').first()
        assert song1.title == "spam"
        db.session.delete(user)
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0
