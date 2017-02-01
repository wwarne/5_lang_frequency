import sys

PUNCTUATION = '!?,.;:()[]»«„“”‘’`"–—'


def load_data(filepath):
    try:
        with open(filepath, mode='r', encoding='utf-8') as data_file:
            for line in data_file:
                yield line
    except OSError:
        yield ''


def count_words(data):
    result = {}
    for line in data:
        for punctuation_mark in PUNCTUATION:
            if punctuation_mark in line:
                line = line.replace(punctuation_mark, ' ')
        for word in line.split():
            word = word.strip().lower()
            if word not in result:
                result[word] = 1
            else:
                result[word] += 1
    return result


def get_most_frequent_words(words_dict):
    return sorted(words_dict.items(), reverse=True, key=lambda one_item: words_dict[one_item[0]])[:10]


def pretty_print(words):
    max_word_len = len(max([word[0] for word in words], key=len))
    row_template = '| {:^%i} | {:^%i} |' % (max_word_len, max_word_len)
    header = row_template.format('Word', 'Count')

    print('-' * len(header))
    print(header)
    print('-' * len(header))

    for one_word in words:
        print(row_template.format(*one_word))

    print('-' * len(header))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit('Script usage: python lang_frequency.py <path to the file>')
    text_lines = load_data(sys.argv[1])
    words_stat = count_words(text_lines)
    if not words_stat:
        sys.exit('File `{}` is empty or unavailable.'.format(sys.argv[1]))
    top_words = get_most_frequent_words(words_stat)
    pretty_print(top_words)
