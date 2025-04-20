from flask_login import LoginManager
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email, EqualTo

from app_factory import app, db

# A single login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'donor_login'  # Default to donor login view

class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password


class Donor(UserMixin, db.Model):
    __tablename__ = 'Donors'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255))
    subscriptions = db.relationship('Subscription', back_populates='donor', lazy=True)
    
    # Adds a type property to identify user type
    @property
    def type(self):
        return 'donor'


class NGO(UserMixin, db.Model):
    __tablename__ = 'NGOs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    
    # Adds a type property to identify user type
    @property
    def type(self):
        return 'ngo'


class Subscription(db.Model):
    __tablename__ = 'Subscriptions'

    id = db.Column(db.Integer, primary_key=True)
    donor_id = db.Column(db.Integer, db.ForeignKey('Donors.id'), nullable=False)
    campaign_id = db.Column(db.Integer, db.ForeignKey('Campaigns.id'), nullable=False)
    donor = db.relationship('Donor', back_populates='subscriptions')
    campaign = db.relationship('Campaign', backref='subscriptions')

    __table_args__ = (
        db.UniqueConstraint('donor_id', 'campaign_id', name='_donor_campaign_uc'),
    )


@login_manager.user_loader
def load_user(user_id):
    # Try to load as a Donor first
    donor = Donor.query.get(int(user_id))
    if donor:
        return donor
    
    # If not a donor, try loading as an NGO
    ngo = NGO.query.get(int(user_id))
    return ngo


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired(), Length(max=250)])
    username = StringField('Username', validators=[InputRequired(), Length(min=4, max=150)])
    email = StringField('Email', validators=[InputRequired(), Email(), Length(max=250)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('password', message='Passwords must match.')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username or Email', validators=[InputRequired(), Length(min=4, max=150)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6)])
    submit = SubmitField('Log In')