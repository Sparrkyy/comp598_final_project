import csv


def get_tweets(filepath, delimiter):
    open_coded_file = open(filepath)
    open_coded_csv = csv.reader(open_coded_file, delimiter=delimiter)
    open_coded_tweets = [line for line in open_coded_csv]
    open_coded_file.close()
    return open_coded_tweets


def get_ids(full_csv):
    ids = {}
    for tweet in full_csv:
        if len(tweet) == 1:

            continue
        ids[tweet[0]] = tweet[3]
    # print(ids)
    return ids


def main():
    fully_annotated = get_tweets("data/fully_annotated.tsv", "\t")
    before_annotation = get_tweets("data/non_coded_tweets.tsv", ",")
    # print(before_annotation)
    fully_annotated_ids = get_ids(fully_annotated)
    before_annotation_ids = get_ids(before_annotation)
    # print(before_annotation_ids)

    for id_key in list(before_annotation_ids):
        if id_key not in fully_annotated_ids:
            print(id_key, before_annotation_ids[id_key])


if __name__ == "__main__":
    main()
