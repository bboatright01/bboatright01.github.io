from os.path import isfile
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import InputRequired, NumberRange, Regexp

from app_factory import db


class Donations(db.Model):
    __tablename__ = 'Donations'

    id = db.Column(db.Integer, primary_key=True)
    DONOR_ID = db.Column(db.Integer, nullable=False)
    CAMPAIGN_ID = db.Column(db.Integer, nullable=False)
    Amount = db.Column(db.Numeric(15,2), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'DONOR_ID': self.DONOR_ID,
            'CAMPAIGN_ID': self.CAMPAIGN_ID,
            'Amount': self.Amount,
            'timestamp': self.timestamp,
        }


class DonationForm(FlaskForm):
    amount = DecimalField('Amount (USD)', validators=[
        InputRequired(),
        NumberRange(min=1, message="Minimum donation is $1.")
    ])
    card_number = StringField('Card Number', validators=[
        InputRequired(),
        Regexp(r'^\d{13,19}$', message="Enter a valid card number.")
    ])
    exp_date = StringField('Expiration Date (MMYY)', validators=[
        InputRequired(),
        Regexp(r'^(0[1-9]|1[0-2])([0-9]{2})$', message="Use MMYY format.")
    ])
    cvv = StringField('CVV', validators=[
        InputRequired(),
        Regexp(r'^\d{3,4}$', message="Enter a valid CVV.")
    ])
    submit = SubmitField('Donate Now')


def total_donated_for_campaign(campaign_id): 
    total_donated = db.session.query(db.func.sum(Donations.Amount)).filter(Donations.CAMPAIGN_ID == campaign_id).scalar()
    return total_donated if total_donated else 0.0

def campaign_donations(campaign_id):
    donations = Donations.query.filter(Donations.CAMPAIGN_ID == campaign_id).all()
    return [donation.to_dict() for donation in donations]

def campaign_donations_by_unique_id(campaign_id):
    donations = Donations.query.filter(Donations.CAMPAIGN_ID == campaign_id).distinct(Donations.DONOR_ID).all()
    return [donation.to_dict() for donation in donations]

def count_donations_by_unique_id(campaign_id):
    count = db.session.query(db.func.count(Donations.DONOR_ID)).filter(Donations.CAMPAIGN_ID == campaign_id).distinct(Donations.DONOR_ID).scalar()
    return count if count else 0.0