from typing import List

def checkio(game_result: List[str]) -> str:
    horiz_a, horiz_b = set(), set()
    board_len = len(game_result)
    result = 0
    rotated_game_result = list(zip(*game_result))
    for i in range(board_len):
        if game_result[i][0] == game_result[i][1] == game_result[i][2] and game_result[i][0] != ".":
            result = game_result[i][0]
        if rotated_game_result[i][0] == rotated_game_result[i][1] == rotated_game_result[i][2] and rotated_game_result[i][0] != ".":
            result = rotated_game_result[i][0]

    for i in range(board_len):
        horiz_a.add(game_result[i][i])
        horiz_b.add(game_result[i][board_len-1-i])
    result = horiz_a.pop() if len(horiz_a) == 1 else result
    result = horiz_b.pop() if len(horiz_b) == 1 else result
    if result == "X":
        return "X"
    elif result == "O":
        return "O"
    else:
        return "D"

if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")