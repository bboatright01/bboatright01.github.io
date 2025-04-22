from os.path import isfile
from app_factory import db
from donations import total_donated_for_campaign
from flask import session

class Campaign(db.Model):
    __tablename__ = 'Campaigns'

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255), nullable=False)
    Description = db.Column(db.Text, nullable=False)
    Country = db.Column(db.String(100), nullable=False)
    NGO_ID = db.Column(db.Integer, nullable=False)
    Funding_Goal = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'Name': self.Name,
            'Description': self.Description,
            'Country': self.Country,
            'NGO_ID': self.NGO_ID,
            'Funding_Goal': self.Funding_Goal
        }

def load_campaigns():
    campaigns = Campaign.query.all()
    return [campaign.to_dict() for campaign in campaigns]


def load_campaigns_by_id(campaign_ids):
    ids = [c["id"] for c in campaign_ids]
    campaigns = Campaign.query.filter(Campaign.id.in_(ids)).all()
    return [campaign.to_dict() for campaign in campaigns]


def load_campaign_by_id(campaign_id):
    campaign = Campaign.query.filter(Campaign.id == campaign_id).first()
    return campaign


def add_new_campaign(data):
    new_campaign = Campaign(
        Name=data['campaign-name'],
        Description=data['campaign-description'],
        Country=data['country'],
        NGO_ID=session['ngo_id'],
        Funding_Goal=int(data['funding-goal'])
    )
    db.session.add(new_campaign)
    db.session.commit()

    return new_campaign


def augment_campaigns(campaigns, PICTURE_EXTENSIONS, IMAGES_FOLDER):
    for campaign in campaigns:
        campaign['Raised'] = int(total_donated_for_campaign(campaign['id']))
        campaign['Image'] = "default.jpg"
        for extension in PICTURE_EXTENSIONS:  # Check if the image file exists in the static/images directory
            if isfile(IMAGES_FOLDER + str(campaign['id']) + '.' + extension):
                campaign['Image'] = str(campaign['id']) + '.' + extension
    return campaigns


def get_campaigns(PICTURE_EXTENSIONS, IMAGES_FOLDER):
    campaigns = load_campaigns()  # Load campaigns from the database
    campaigns = augment_campaigns(campaigns, PICTURE_EXTENSIONS, IMAGES_FOLDER) # Augment the campaigns with additional data
    return campaigns

