def unpack_list(array):
    result = []
    if type(array) is list:
        for item in array:
            if type(item) is list:
                result.extend(unpack_list(item))
            else:
                result.append(item)
    else:
        result.append(array)
    return result


def flat_list(array):
    result = []
    for i, item in enumerate(array):
        res_unpack = unpack_list(item)
        result.extend(res_unpack)
    return result

if __name__ == '__main__':
    # assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    # assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')