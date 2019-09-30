VOWELS = "aeiouy"


def translate(phrase):
    result = ''
    item = 0
    while item < len(phrase):
        result += phrase[item]
        if phrase[item] not in VOWELS and phrase[item] != ' ':
            item += 2
        else:
            item += 1
    map_dict = dict(zip(VOWELS, (i * 3 for i in VOWELS)))
    for k, v in map_dict.items():
        result = result.replace(v, k)
    return result


if __name__ == '__main__':
    print("Example:")
    # print(translate("hieeelalaooo"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")