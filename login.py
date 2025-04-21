from flask_login import LoginManager
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email, EqualTo

from app_factory import app, db

donor_login_manager = LoginManager()
donor_login_manager.init_app(app)
donor_login_manager.login_view = 'login'

# ngo_login_manager = LoginManager()
# ngo_login_manager.login_view = 'ngo_login'
# ngo_login_manager.init_app(app)


class Donor(UserMixin, db.Model):
    __tablename__ = 'Donors'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255))
    subscriptions = db.relationship('Subscription', back_populates='donor', lazy=True)


class NGO(UserMixin, db.Model):
    __tablename__ = 'NGOs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    description = db.Column(db.Text)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(64))
    address = db.Column(db.String(256))

    def to_dict(self):
        return {
            'id': self.id,
            'Name': self.name,
            'Description': self.description,
            'username': self.username,
            'password': self.password,
            'Email': self.email,
            'Address': self.address
        }


def get_ngo_by_id(ngo_id):
    ngo = NGO.query.filter(NGO.id == ngo_id).first()
    return ngo.to_dict() if ngo else None


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


# @ngo_login_manager.user_loader
# def load_ngo(user_id):
#     return NGO.query.get(int(user_id))


@donor_login_manager.user_loader
def load_user(user_id):
    return Donor.query.get(int(user_id))


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