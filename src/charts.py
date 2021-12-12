import argparse
import json

import stylecloud

def generate(words, output):
    res = " ".join(str(item) for item in words)
    stylecloud.gen_stylecloud(
        text=res,
        size=1080,
        # font_path='msyh.ttc',
        # palette='cartocolors.qualitative.Pastel_7',
        gradient='horizontal',
        # icon_name='fab fa-weixin',
        output_name=output)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--input")
    args = parser.parse_args()
    input_file = open(args.input)
    inputs = json.loads(input_file.read())
    for text in inputs:
        output = text.replace('/', '_') + ".png"
        generate(inputs[text], output)

if __name__ == '__main__':
    main()