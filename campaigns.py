from os.path import isfile

from app_factory import db


class Campaign(db.Model):
    __tablename__ = 'campaigns'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    country = db.Column(db.String(100), nullable=False)
    ngo_id = db.Column(db.Integer, nullable=False)
    funding_goal = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'Name': self.name,
            'Description': self.description,
            'Country': self.country,
            'NGO_ID': self.ngo_id,
            'Funding_Goal': self.funding_goal
        }

def load_campaigns():
    campaigns = Campaign.query.all()
    return [campaign.to_dict() for campaign in campaigns]


def load_campaigns_by_id(campaign_ids):
    ids = [c["id"] for c in campaign_ids]
    campaigns = Campaign.query.filter(Campaign.id.in_(ids)).all()
    return [campaign.to_dict() for campaign in campaigns]


def add_new_campaign(data):
    new_campaign = Campaign(
        name=data['campaign-name'],
        description=data['campaign-description'],
        country=data['country'],
        ngo_id=1,  # Make dynamic later
        funding_goal=int(data['funding-goal'])
    )
    db.session.add(new_campaign)
    db.session.commit()
    return new_campaign


def augment_campaigns(campaigns, PICTURE_EXTENSIONS, IMAGES_FOLDER):
    for campaign in campaigns:
        campaign['Raised'] = 10000  # Example data for testing; to be replaced with database
        campaign['Image'] = "default.jpg"  # Example data for testing; to be replaced with database
        for extension in PICTURE_EXTENSIONS:  # Check if the image file exists in the static/images directory
            if isfile(IMAGES_FOLDER + str(campaign['id']) + '.' + extension):
                campaign['Image'] = str(campaign['id']) + '.' + extension
    return campaigns


def get_campaigns(PICTURE_EXTENSIONS, IMAGES_FOLDER):
    campaigns = load_campaigns()  # Load campaigns from the database
    campaigns = augment_campaigns(campaigns, PICTURE_EXTENSIONS, IMAGES_FOLDER) # Augment the campaigns with additional data
    return campaigns

