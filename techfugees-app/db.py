from techfugees import app
from techfugees import db, bcrypt

if __name__ == "__main__":
    from techfugees.models import User, Landlord, Tenant
    from techfugees.models import Post, Review
    db.create_all()

    for i in range (10):
        hashed_password = bcrypt.generate_password_hash("password").decode('utf-8')
        tenant = Tenant(username="tenant"+str(i), email="tenant"+str(i)+"@example.com", password=hashed_password)
        landlord = Landlord(username="landlord"+str(i), email="landlord"+str(i)+"@example.com", password=hashed_password)
        db.session.add(tenant)
        db.session.add(landlord)
        db.session.commit()

