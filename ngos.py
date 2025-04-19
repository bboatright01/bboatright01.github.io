from os.path import isfile

from app_factory import db

class NGOS(db.Model):
    __tablename__ = 'NGOS'

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(128))
    Description = db.Column(db.Text)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    Email = db.Column(db.String(64))
    Address = db.Column(db.String(256))

    def to_dict(self):
        return {
            'id': self.id,
            'Name': self.Name,
            'Description': self.Description,
            'username': self.username,
            'password': self.password,
            'Email': self.Email,
            'Address': self.Address
        }
    
def get_ngo_by_id(ngo_id):
    ngo = NGOS.query.filter(NGOS.id == ngo_id).first()
    return ngo.to_dict() if ngo else None