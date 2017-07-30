import csv
from collections import defaultdict
from decimal import Decimal
import sys


def parse_csv(file_name: str):
    """
    Expects a csv with two rows; the first containing a category, and the second containing a sentence in that category.
    """
    category_to_sentence_details_map = {}

    with open(file_name) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            tokenized_sentence = tokenize(row[1])
            if row[0] not in category_to_sentence_details_map:
                category_to_sentence_details_map[row[0]] = defaultdict(int)

            for word in tokenized_sentence:
                category_to_sentence_details_map[row[0]][word] += 1

    return category_to_sentence_details_map


def tokenize(sentence: str):
    return sentence.lower().split()


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


def main():
    csv_file_path = sys.argv[1]
    category_to_token_map = parse_csv(csv_file_path)

    while 1:
        new_input = input('Enter a new sentence: ')
        tokenized_input = tokenize(new_input)

        max_probablility = float('-Inf')
        most_likely_category = None
        for category, token_counts in category_to_token_map.items():
            probability = calculate_probablility(tokenized_input, token_counts)
            if probability > max_probablility:
                max_probablility = probability
                most_likely_category = category

        print('Most likely category: {}'.format(most_likely_category))


if __name__ == '__main__':
    main()
