#!/usr/bin/python
import csv
import sys
import re


def parse_text(text):
    SEPARATOR = ' '
    # Try to remove links
    #
    text = re.sub('http[^ ]*', SEPARATOR, text)

    # Replace &amp; with and, and &gt; with greater than
    #
    text = text.replace("&amp;", "and")
    text = text.replace("&gt;", "greaterthan")

    # Replace punctuation with a unique character to separate sentences.
    #
    splitters = ".?!"
    for i in splitters[:-1]:
        text = text.replace(i, splitters[-1])

    # Replace non-alpha and non-punctuation characters with spaces.
    #
    text = re.sub('[^!a-zA-Z]+', SEPARATOR, text)

    # Start splitting
    #
    sentences = text.split(splitters[-1])
    data = []
    for s in sentences:
        s = [w.lower() for w in s.split(SEPARATOR) if len(w) != 0]
        if len(s) != 0:
            data.append(s)
    return data


def main():
    tweets_file = sys.argv[1] if len(sys.argv) >= 2 else "tweets.csv"
    f = open(tweets_file, 'r')
    reader = csv.DictReader(f)

    data = []
    for tweet in reader:
        data.extend(parse_text(tweet['text']))

    print("data = %s" % repr(data))


if __name__ == "__main__":
    main()
