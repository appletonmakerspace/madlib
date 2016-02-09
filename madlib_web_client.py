import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import Madlib

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
db = SQLAlchemy(app)

db.create_all()

m = Madlib("A cheese madlib", "Here is where the body of this madlib would be if this was a complete example.")

db.session.add(m)
db.session.commit()

print(Madlib.query.all())

@app.route("/")
def hello():
    return "Hello world!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
