from techfugees import app
from techfugees import db

if __name__ == "__main__":
    from techfugees.models import User, Landlord, Refugee
    from techfugees.models import Post
    db.create_all()

    for i in range (10):
        hashed_password = bcrypt.generate_password_hash("password").decode('utf-8')
        if (i%3 == 0):
            user = Refugee(username="user"+str(i), email="user"+str(i)+"@example.com", password=hashed_password)
        else:
            user = Landlord(username="landlord"+str(i), email="landlord"+str(i)+"@example.com", password=hashed_password)
        db.session.add(user)
        db.session.commit()