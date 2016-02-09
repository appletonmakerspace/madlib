import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
db = SQLAlchemy(app)
db.create_all()

from app.models import Madlib
m = Madlib("A cheese madlib", "Here is where the body of this madlib would be")

db.session.add(m)
db.session.commit()

print(Madlib.query.all())


@app.route("/")
def hello():
    return "Hello world!"
