import sys

from calculations import calculate_probablility
from input_parser import parse_csv, tokenize


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
