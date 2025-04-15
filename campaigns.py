from app_factory import db

class Campaign(db.Model):
    __tablename__ = 'campaigns'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    country = db.Column(db.String(100), nullable=False)
    ngo_id = db.Column(db.Integer, nullable=False)
    funding_goal = db.Column(db.Integer, nullable=False)


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