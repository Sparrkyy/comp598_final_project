import argparse

import pandas as pd

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--input")
    args = parser.parse_args()
    df = pd.read_csv(args.input,  error_bad_lines=False)
    categories = ["actor/character talk", "advertisement", "comparison", "release", "review", "scene/plot talk", "too little info", "watching"]
    for category in categories:
        count = len(df[df['coding'] == category])
        negative = len(df[(df['coding'] == category) & (df['sentiment'] == 'negative')])
        neutral = len(df[(df['coding'] == category) & (df['sentiment'] == 'neutral')])
        positive = len(df[(df['coding'] == category) & (df['sentiment'] == 'positive')])
        print(category)
        print("positive: ", positive/count*100)
        print("neutral: ", neutral/count*100)
        print("negative: ", negative/count*100)
        print()



if __name__ == '__main__':
    main()