import random


class Madlib:
    '''
    This class generates the madlib from word lists.
    '''
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
