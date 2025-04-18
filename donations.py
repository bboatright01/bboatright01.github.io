from os.path import isfile

from app_factory import db

class Donations(db.Model):
    __tablename__ = 'Donations'

    id = db.Column(db.Integer, primary_key=True)
    DONOR_ID = db.Column(db.Integer, nullable=False)
    CAMPAIGN_ID = db.Column(db.Integer, nullable=False)
    Amount = db.Column(db.Numeric(15,2), nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'DONOR_ID': self.DONOR_ID,
            'CAMPAIGN_ID': self.CAMPAIGN_ID,
            'Amount': self.Amount,
            'timestamp': self.timestamp,
        }
    
def total_donated_for_campaign(campaign_id): 
    total_donated = db.session.query(db.func.sum(Donations.Amount)).filter(Donations.CAMPAIGN_ID == campaign_id).scalar()
    return total_donated if total_donated else 0.0