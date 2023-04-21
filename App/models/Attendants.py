from App.database import db
from App.models import Ship, Intern

class Attendants(db.Model):
    ship_id = db.Column(db.Integer, db.ForeignKey('ship.id'), primary_key=True, autoincrement=False)
    intern_id = db.Column(db.Integer, db.ForeignKey('intern.school_id'), primary_key=True, nullable=False)
#   intern = db.relationship('intern', backref=db.backref('attendees', lazy='joined'))
 
    def __init__(self, ship_id, intern_id):
        self.ship_id = ship_id
        self.ship_id = intern_id
    


    def get_json(self):
        return {
        "Internship ID": self.ship_id,
        "Internship Name": self.ship_id.name,
        "Attendants": self.cat_list()
        }
    