from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
use_decimal_type = False


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime)
    modified = db.Column(db.DateTime)

    username = db.Column(db.String(100), unique=True)


class Keg(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime)
    modified = db.Column(db.DateTime)

    description = db.Column(db.String(100))
    estimated_cost = db.Column(db.Numeric(13, 2, asdecimal=use_decimal_type))

    date_funded = db.Column(db.DateTime)
    date_tapped = db.Column(db.DateTime)
    date_kicked = db.Column(db.DateTime)

    backer_id = db.Column(db.Integer, db.ForeignKey(User.id))


class Pledge(db.Model):
    keg_id = db.Column(db.Integer, db.ForeignKey(Keg.id), primary_key=True)
    pledger_id = db.Column(db.Integer, db.ForeignKey(User.id), primary_key=True)
    created = db.Column(db.DateTime)
    modified = db.Column(db.DateTime)

    amount = db.Column(db.Numeric(13, 2, asdecimal=use_decimal_type), nullable=False)
