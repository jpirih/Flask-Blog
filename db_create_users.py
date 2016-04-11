from app import app, db
from models import User

# add sample users
db.session.add(User('admin', 'janko.pirih@gmail.com','student15'))
db.session.add(User('kekec', 'g.kekec@gmail.com','kekec123'))

# commit changes to db
db. session.commit()