import csv


'''
tweets = open(args.input)
tweets_csv = csv.reader(tweets)
tweets_arr = [line for line in tweets_csv]
'''


def get_tweets(filepath, delimiter):
    open_coded_file = open(filepath)
    open_coded_csv = csv.reader(open_coded_file, delimiter=delimiter)
    open_coded_tweets = [line for line in open_coded_csv]
    open_coded_file.close()
    return open_coded_tweets


def main():
    open_coded_tweets = get_tweets("data/Open Coding - Sheet1.tsv", "\t")
    all_tweets = get_tweets("data/collection.csv", ",")
    tweets_still_need_to_code = [tweet for tweet in all_tweets]
    for tweet in open_coded_tweets:
        tweet_id = tweet[0]
        for tweet2 in tweets_still_need_to_code:
            tweet2_id = tweet2[0]
            if tweet2_id == tweet_id:
                tweets_still_need_to_code.remove(tweet2)
                break

    dump_of_non_coded_tweets = open("data/non_coded_tweets.tsv", "w")
    dump_of_non_coded_tweets.write(
        "id,author_id,created_at,text,coding,sentiment\n")
    #dump_csv = csv.writer(dump_of_non_coded_tweets, delimiter="\t")
    for line in tweets_still_need_to_code:
        line = ["\"" + item + "\"" for item in line]
        new_line = ",".join(line)
        fixed_line = ""
        for ch in new_line:
            if ch == "\n":
                continue
            fixed_line += ch
        dump_of_non_coded_tweets.write(fixed_line + "\n")
    dump_of_non_coded_tweets.close()


if __name__ == "__main__":
    main()
