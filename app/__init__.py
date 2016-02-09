import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


from app.models import Madlib
db.create_all()
db.session.commit()

m = Madlib("A cheese madlib", "Here is where the body of this madlib would be")

db.session.add(m)
db.session.commit()

print(Madlib.query.all())


@app.route("/")
def hello():
    return "Hello world!"
