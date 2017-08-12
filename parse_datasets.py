import csv


def main():
    with open("test_data.csv", "w") as csv_output:
        writer = csv.writer(csv_output)
        with open("clickbait_data", "r", encoding="utf-8") as clickbait_input:
            for line in clickbait_input:
                writer.writerow(["clickbait", line])

        with open("non_clickbait_data", "r", encoding="utf-8") as non_clickbait_input:
            for line in non_clickbait_input:
                writer.writerow(["not clickbait", line])

if __name__ == '__main__':
    main()