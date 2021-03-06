from techfugees import app
from techfugees import db

if __name__ == "__main__":
    from techfugees.models import User, Landlord, Refugee 
    from techfugees.models import Post
    db.create_all()