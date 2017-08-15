#!/usr/bin/env python
import csv


def write_csv(file_to_read, classification, training_csv_writer):
    for line in file_to_read:
        text = line.rstrip()
        if not text:
            continue
        training_csv_writer.writerow([classification, text])


if __name__ == "__main__":
    training_file = open("train.csv", "w")
    clickbait_file = open("clickbait_data", "r")
    non_clickbait_file = open("non_clickbait_data", "r")

    training_writer = csv.writer(training_file)

    write_csv(clickbait_file, "clickbait", training_writer)
    write_csv(non_clickbait_file, "non clickbait", training_writer)

    training_file.close()
    clickbait_file.close()
    non_clickbait_file.close()
