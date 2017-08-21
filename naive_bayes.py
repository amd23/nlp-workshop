import csv
from collections import Counter
import re
import sys


class Classifier(object):
    def __init__(self):
        self.trained_data = {}

    def tokenize(self, sentence: str):
        cleaned_string = re.sub("[\W]", " ", sentence)
        return cleaned_string.lower().split()

    def _calculate_probablility(self, classification: str, tokens: list):
        """
        Calculates the probability of `tokens` being in `classification`
        """
        return 0

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

    def classify(self, raw_input: str):
        tokens = self.tokenize(raw_input)

        max_probablility = float("-Inf")
        most_likely_classification = None
        for classification, token_counts in self.trained_data.items():
            probability = self._calculate_probablility(classification, tokens)
            if probability > max_probablility:
                max_probablility = probability
                most_likely_classification = classification

        if max_probablility == Decimal("0"):
            raise Exception("No classification found")

        return most_likely_classification


def main():
    csv_file_path = sys.argv[1]
    classifier = Classifier()
    classifier.train(csv_file_path)

    while 1:
        new_input = input('Enter a new sentence: ')
        print('Most likely category: {}'.format(classifier.classify(new_input)))
        print('')


if __name__ == '__main__':
    main()
