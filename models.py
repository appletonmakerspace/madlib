import random
from app import db

class Madlib(db.Model):
    '''
    This class generates the madlib from word lists.
    '''
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    create_date = db.Column(db.DateTime)

    def __init__(self, title, body, create_date=None):
        self.title = title
        self.body = body
        if create_date is None:
            create_date = datetime.utcnow()
        self.create_date = create_date

    def __repr__(self):
        return '<Madlib %r>' % self.title

    def get_madlib(self):
        madlib = """
        Once there was a {0}. It {1} at the {2}.
        Then because of its {3} it {4}. Wow! You sure are {5}!
        Thanks! I {6} you very much.
        """
        nouns = ['cheesecakes', 'bicycle', 'park', 'computer']
        verbs = ['watched tv', 'voted', 'fell over']
        adjectives = ['smelly', 'slimy', 'soft', 'loud']

        output = madlib.format(
            random.choice(nouns),
            random.choice(verbs),
            random.choice(nouns),
            random.choice(nouns),
            random.choice(verbs),
            random.choice(adjectives),
            random.choice(adjectives)
        )
        return output
