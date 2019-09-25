from collections import Counter


def checkio(text: str) -> str:
    letter_count = dict(Counter(filter(str.isalpha, text.lower())).most_common())
    most_freq_letter = next(iter(letter_count.values()))
    return sorted([k for k, v in letter_count.items() if v == most_freq_letter])[0]


if __name__ == '__main__':
    print("Example:")
    print(checkio("One"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l"
    assert checkio("How do you do?") == "o"
    assert checkio("One") == "e"
    assert checkio("Oops!") == "o"
    assert checkio("AAaooo!!!!") == "a"
    assert checkio("abe") == "a"
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a"
    print("The local tests are done.")