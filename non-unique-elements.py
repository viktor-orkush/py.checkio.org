# Your optional code here
# You can import some modules or create additional functions
from collections import Counter


def checkio(data: list) -> list:
    data_counter = dict(Counter(data).most_common())
    [data.remove(k) for k, v in data_counter.items() if v == 1]
    return data

# Some hints
# You can use list.count(element) method for counting.
# Create new list with non-unique elements
# Loop over original list


print (checkio([1, 2, 3, 1, 3]))

if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3]  # "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == []  # "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5]  # "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9]  # "4th example"
    print("It is all good. Let's check it now")
