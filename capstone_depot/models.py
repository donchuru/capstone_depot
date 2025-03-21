'''
To edit anything on the database, run the following commands in the Python shell:

from capstone_depot import create_app, db
app = create_app()
app.app_context().push()

If you want to edit the schema:
db.drop_all()
db.create_all()
'''


import jwt, json
from datetime import datetime, timezone, timedelta
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from capstone_depot import db, login_manager
from flask_login import UserMixin
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy import JSON

@login_manager.user_loader  # decorator so that the function knows this is its job
def load_user(user_id):
    return User.query.get(int(user_id))

# each class is a table
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(), nullable=False, default='https://res.cloudinary.com/dxpmu1c0z/image/upload/v1689164141/default_tu17zb.png')
    password = db.Column(db.String(60), nullable=True)  # Making nullable for OAuth users
    posts = db.relationship('Post', backref='author', lazy=True)

    # OAuth fields
    oauth_provider = db.Column(db.String(20), nullable=True)  # 'google', etc.
    oauth_id = db.Column(db.String(100), nullable=True)  # Provider's unique ID
    oauth_token = db.Column(db.Text, nullable=True)  # OAuth token
    oauth_data = db.Column(MutableDict.as_mutable(JSON), nullable=True)  # Additional OAuth data

    ''' reset email and password '''

    def get_reset_token(self, expires_sec=1800):
        # s = Serializer(app.config['SECRET_KEY'], expires_sec)
        # return s.dumps({'user_id': self.id}).decode('utf-8')
        s = jwt.encode({"exp": datetime.now(tz=timezone.utc) + timedelta(seconds=expires_sec), "user_id":self.id}, current_app.config['SECRET_KEY'], algorithm="HS256")
        return s


    @staticmethod
    def verify_reset_token(token):
        # s = Serializer(app.config['SECRET_KEY'])
        # try:
        #     user_id = s.loads(token)['user_id']
        # except:
        #     return None
        # return User.query.get(user_id)
        try:
            s = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            user_id = s['user_id']
        except:
            return None
        return User.query.get(user_id)


    # how our object is printed out
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    year = db.Column(db.Integer(), nullable=False)
    team_members = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(), nullable=False)
    content = db.Column(db.Text, nullable=False)
    link = db.Column(db.Text, nullable=True)
    poster = db.Column(db.String(), nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

    def get_team_members(self):
        """Return team members as a string or parse JSON if possible"""
        try:
            return json.loads(self.team_members)
        except:
            return self.team_members

    def add_team_member(self, name, linkedin_url):
        team_members = self.get_team_members()
        team_members.append({'name': name, 'linkedin_url': linkedin_url})
        self.team_members = json.dumps(team_members)

    def remove_team_member(self, name):
        team_members = self.get_team_members()
        team_members = [tm for tm in team_members if tm['name'] != name]
        self.team_members = json.dumps(team_members)
