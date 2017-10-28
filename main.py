#!/usr/bin/python
from data import data
from train import train_model
from train_n import train_model_n
import sys


def main():
    if len(sys.argv) == 1:
        mm, ec = train_model(data)
        print(' '.join(w for w in mm.random_sequence(ec)[:-1]))
    else:
        n = int(sys.argv[1])
        assert n > 0

        mm, ec = train_model_n(data, n)
        seq = mm.random_sequence(ec)
        prefix = ' '.join(seq[0][:-1])
        print(prefix + ' ' + ' '.join(s[-1] for s in seq[:-1]))


if __name__ == "__main__":
    main()
