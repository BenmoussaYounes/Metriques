


def cosine_similarity(self, x, y):
    """ return cosine similarity between two lists """

    numerator = sum(a * b for a, b in zip(x, y))
    denominator = self.square_rooted(x) * self.square_rooted(y)
    return round(numerator / float(denominator), 3)