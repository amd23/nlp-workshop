import csv
from collections import Counter
from decimal import Decimal
import sys


class Classifier(object):
    def __init__(self):
        self.trained_data = {}

    def train(self, file_name: str):
        """
        Expects a csv with two rows; the first containing a category, and the second containing a sentence in that category.
        """
        category_to_token_count_map = {}

        with open(file_name, encoding="utf8") as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                tokenized_sentence = self.tokenize(row[1])

                if row[0] not in category_to_token_count_map:
                    category_to_token_count_map[row[0]] = Counter()

                for word in tokenized_sentence:
                    category_to_token_count_map[row[0]][word] += 1

        self.trained_data = category_to_token_count_map

    def tokenize(self, sentence: str):
        return sentence.lower().split()

    def _calculate_probablility(self, classification: str, tokens: list, delta=0.01):
        """
        Calculates the add-delta probability P(tokens | details)
        """
        if classification not in self.trained_data:
            return 0

        token_counts = self.trained_data[classification]
        total_words_in_category = sum(val for val in token_counts.values())
        probability = Decimal('1')
        for token in tokens:
            counts = token_counts.get(token, delta)
            token_probability = Decimal(counts / total_words_in_category)
            probability = probability * token_probability

        return probability

    def classify(self, raw_input: str):
        tokens = self.tokenize(raw_input)

        max_probablility = float("-Inf")
        most_likely_classification = None
        for classification, token_counts in self.trained_data.items():
            probability = self._calculate_probablility(classification, tokens)
            if probability > max_probablility:
                max_probablility = probability
                most_likely_classification = classification

        return most_likely_classification


def main():
    csv_file_path = sys.argv[1]
    classifier = Classifier()
    classifier.train(csv_file_path)

    while 1:
        new_input = input('Enter a new sentence: ')
        print('Most likely category: {}'.format(classifier.classify(new_input)))


if __name__ == '__main__':
    main()
