# word_utils.py - part of the WordGame 


from collections import Counter

import random

WORDS_FILE = "words.txt"
BIG_WORDS = "bigwords.txt"
ALL_WORDS = "allwords.txt"


def pre_process_words() -> None:
    """Take the big list of words and remove small words (< 4 chars).

    Split the file into two sub-files: bigwords.txt and allwords.txt,
    noting that all data is converted to lowercase."""
    with open(WORDS_FILE) as rawdata:
        with open(ALL_WORDS, "w") as allwords:
            with open(BIG_WORDS, "w") as bigwords:
                for word in rawdata:
                    word = word.lower().strip()  # Remove pesky \n.
                    word = word.replace(
                        "'s", ""
                    )  # Remove any trailing 's at end of word.
                    if len(word) > 7:
                        print(word, file=bigwords)
                    if len(word) > 3:
                        print(word, file=allwords)


def get_source_word() -> str:
    """Randomly grab a source word from the bigwords file."""
    with open(BIG_WORDS) as bf:
        word = random.choice(bf.readlines())
    return word.strip()  # Remove that pesky \n.


def check_letters(sourceword, check_word) -> list:
    """Check one word (check_word) is "inside" another (source_word).

    By "inside" we mean that the number and value of the letters
    in the check_word must be in the sourceword as per the
    Word Game rules. A list of tuples is returned where
    each (letter, bool) tuple provides validity."""
    letter_status = []
    cw_counter = Counter(check_word)
    sw_counter = Counter(sourceword)
    for k, v in cw_counter.items():
        if sw_counter[k] < v:
            letter_status.append((k, False))
        else:
            letter_status.append((k, True))
    return letter_status


def check_size(words, howbig=4) -> list:
    """Checks a list of words to ensure they are of a certain size.

    Returns a list of tuples of (word, bool) to indicate success."""
    lengths_ok = []
    for word in words:
        if len(word) >= howbig:
            lengths_ok.append((word, True))
        else:
            lengths_ok.append((word, False))
    return lengths_ok


def duplicates(words) -> list:
    """Returns True if the list contains any duplicates."""
    return bool(len(words) > len(set(words)))


def check_not_sourceword(words, sourceword) -> list:
    """Checks a list of words to ensure none are the sourceword.

    Returns a list of words to indicate match."""
    return [word for word in words if word == sourceword]
