import argparse
import re
import os
import sys
from collections import Counter


FIND_EVERY_WORD = re.compile(r'\w+', re.UNICODE)


def fetch_lines_from_file(filepath):
    yield from open(filepath, mode='r', encoding='utf-8')


def split_lines_to_words(lines):
    for line in lines:
        for match in FIND_EVERY_WORD.finditer(line):
            yield match.group(0).lower()


def count_words_from_file(filepath):
    result = Counter()
    lines = fetch_lines_from_file(filepath)
    words = split_lines_to_words(lines)
    result.update(words)
    return result


def print_words(counted_words):
    print('| {:<14} | {:<11} |'.format('WORD', 'COUNT'))
    for word, count in counted_words:
        print('| {:<14} | {:<11} |'.format(word, count))


def create_parser():
    result = argparse.ArgumentParser()
    result.add_argument('filepath', help='Path to a file')
    result.add_argument('number', default=10, type=int, help='How many words to print (default is 10)', nargs='?')
    return result

if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    if not os.path.isfile(namespace.filepath):
        sys.exit('There is no file called {}'.format(namespace.filepath))

    all_words_counted = count_words_from_file(namespace.filepath)
    top_words = all_words_counted.most_common(namespace.number)
    print_words(top_words)
