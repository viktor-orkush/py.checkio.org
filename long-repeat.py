def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    length_line = len(line)
    if length_line <= 1:
        return length_line
    else:
        count_list = []
        letter_count = 1
        prev_letter = line[0]
        for item in range(1, length_line):
            if prev_letter == line[item]:
                letter_count += 1
                if item == len(line) - 1:
                    count_list.append(letter_count)
            else:
                count_list.append(letter_count)
                prev_letter = line[item]
                letter_count = 1
    return max(count_list) if count_list else 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('a') == 1, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
