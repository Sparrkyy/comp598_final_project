import argparse
import csv
import random
# python3.9 src/get_random_sample.py -i data/collection.csv -n 200 -o data/open_coding.csv


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input")
    parser.add_argument("-o", "--output")
    parser.add_argument("-n", "--number")
    args = parser.parse_args()

    tweets = open(args.input)
    tweets_csv = csv.reader(tweets)
    tweets_arr = [line for line in tweets_csv]
    sample = random.sample(tweets_arr, int(args.number))
    tweets.close()

    dump_file = open(args.output, "w")
    dump_file.write(",".join(tweets_arr[0]) + "\n")
    for line in sample[1:]:
        line = ["\"" + item + "\"" for item in line]
        new_line = ",".join(line)
        fixed_line = ""
        for ch in new_line:
            if ch == "\n":
                continue
            fixed_line += ch

        dump_file.write(fixed_line + "\n")
    dump_file.close()


if __name__ == "__main__":
    main()
