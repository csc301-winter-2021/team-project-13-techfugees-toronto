from techfugees import app
from techfugees import db

if __name__ == "__main__":
    from techfugees.models import User, Post, Refugee
    db.create_all()