import csv
from collections import defaultdict


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
