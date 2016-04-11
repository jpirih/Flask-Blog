from project import db
from project.models import BlogPost

# create database and the db tables


# insert data
db.session.add(BlogPost('Good','I am good',2))
db.session.add(BlogPost('Well', 'I am well',2))
db.session.add(BlogPost('Super', 'This is super',3))
db.session.add(BlogPost('Test', 'To je test',3))

# commit changes
db.session.commit()