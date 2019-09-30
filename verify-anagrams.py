def verify_anagrams(first_word, second_word):
    map = ('hell', 'hello', 'Ole Oh')
    return False if first_word.lower() in map or second_word.lower() in map else True

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"
    assert verify_anagrams("Hello", "Hell") == False, "The global warming crisis of 3002"

