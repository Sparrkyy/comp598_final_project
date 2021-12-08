import argparse
import csv
import json
# python3 src/compile_word_counts.py -o data/output.json -d data/clean_dialog.csv


stopwords = {}
stopwords_file = open("data/stopwords.txt")
for line in stopwords_file:
    if line[0] == '#':
        continue
    stopwords[line[:-1]] = True
stopwords_file.close()


def add_to_frequency_dict(the_dict, word):

    if word not in the_dict:
        the_dict[word] = 1
    else:
        the_dict[word] += 1


def add_line_to_frequency_dict(the_dict, line):
    replace_chars = "()[],-.?!:;#&"
    replaced_line = ""
    for ch in line:
        if ch in replace_chars:
            replaced_line += " "
        else:
            replaced_line += ch.lower()
    # print(replaced_line)
    words = replaced_line.split(" ")
    for word in words:
        if word in stopwords or not word.isalpha():
            # print(word)
            continue
        add_to_frequency_dict(the_dict, word.lower())


def get_counts(dialog_file):
    # Create the pony dict
    catagory_words = {}
    all_words = {}

    # getting the dialog
    tweets = open(dialog_file)
    tweets_csv = csv.reader(tweets, delimiter="\t")
    skip = True
    for tweet in tweets_csv:
        if skip:
            skip = False
            continue
        tweet_text = tweet[3]
        tweet_category = tweet[4].strip()
        if tweet_category not in catagory_words:
            catagory_words[tweet_category] = {}
        add_line_to_frequency_dict(catagory_words[tweet_category], tweet_text)
        add_line_to_frequency_dict(all_words, tweet_text)

    tweets.close()

    for key in catagory_words:
        to_delete = []
        for keyword in catagory_words[key]:
            if all_words[keyword] < 5:
                to_delete.append(keyword)
        for keyword in to_delete:
            del catagory_words[key][keyword]

    print(list(catagory_words))
    return catagory_words


def main():
    # Parser set up
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output')
    parser.add_argument('-d', '--dialog')
    args = parser.parse_args()
    if not args.output or not args.dialog:
        print("improper arguments")
        return

    pony_words = get_counts(args.dialog)

    output_file = open(args.output, "w")
    output_file.write(json.dumps(pony_words, indent=4, sort_keys=True))
    output_file.close()


if __name__ == "__main__":
    main()
