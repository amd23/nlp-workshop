from decimal import Decimal


def calculate_probablility(tokens: list, token_counts: dict, delta=0.01):
    """
    Calculates the add-delta probability P(tokens | details)
    """
    total_words_in_category = len(token_counts.keys())
    probability = Decimal('1')
    for token in tokens:
        counts = token_counts.get(token, delta)
        token_probability = Decimal(counts / total_words_in_category)
        probability = probability * token_probability

    return probability
