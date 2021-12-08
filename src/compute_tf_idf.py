import argparse
import json
import math

#  python3 src/compute_pony_lang.py -c data/output.json


def get_idf(pony_counts, word):
    return math.log(8/get_number_of_ponies_using_word(pony_counts, word))


def get_number_of_ponies_using_word(pony_counts, word):
    number_of_ponies = 0
    for key in pony_counts:
        if word in pony_counts[key]:
            number_of_ponies += 1
    # print(number_of_ponies)
    return number_of_ponies


def get_tf(pony_counts, pony, word):
    return pony_counts[pony][word]


def get_tf_idf(pony_counts, pony, word):
    return get_tf(pony_counts, pony, word) * get_idf(pony_counts, word)


def mapping_data(n):
    return n[0]


def get_final_data(pony_counts):
    semi_final_data = {}
    for ponykey in pony_counts:
        arr = []
        for word in pony_counts[ponykey]:
            arr.append([word, get_tf_idf(pony_counts, ponykey, word)])
        arr.sort(key=lambda x: -x[1])
        semi_final_data[ponykey] = arr
    return semi_final_data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--pony_counts")
    parser.add_argument("-n", "--num_words")
    args = parser.parse_args()
    # get pony word counts
    words_used_count = {}
    pony_file = open(args.pony_counts)
    pony_counts = json.loads(pony_file.read())
    for pony_name_key in pony_counts:
        for word_key in pony_counts[pony_name_key]:
            if word_key in words_used_count:
                words_used_count[word_key] += 1
            else:
                words_used_count[word_key] = 1

    # get the final data
    final_data = {}
    semi_final_data = get_final_data(pony_counts)
    # print(semi_final_data)
    for ponykey in semi_final_data:
        words_only = map(mapping_data, semi_final_data[ponykey])
        words_only_arr = list(words_only)
        final_data[ponykey] = words_only_arr[0:int(args.num_words)]

    print(json.dumps(final_data, indent=4))


if __name__ == "__main__":
    main()
