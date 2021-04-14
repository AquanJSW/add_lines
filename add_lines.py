#!/usr/bin/env python3
import argparse
import os
import sys
from typing import Iterable, List


def argparser():
    parser = argparse.ArgumentParser(
        description="Add lines to the end of a file with some additional format works."
    )
    parser.add_argument("path", help="Target file path to write to.")
    parser.add_argument("lines", nargs='+', help="Lines to be writen.")
    parser.parse_args()


def all_strip(it: Iterable[str]) -> List:
    ret = []
    for i in it:
        i = i.strip()
        if i:
            ret.append(i)
    return ret


def main():
    path = sys.argv[1]
    if not os.path.isfile(path):
        raise FileNotFoundError
    lines = sys.argv[2:]
    lines = all_strip(lines)
    with open(path, 'r') as fr:
        rules = all_strip(fr.readlines())
    with open(path, 'w') as fr:
        fr.writelines([i + '\n' for i in set(rules + lines)])


if __name__ == '__main__':
    argparser()
    main()
