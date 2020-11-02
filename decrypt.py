from typing import Iterable, List, Tuple


def make_shift(s: str, shift: int) -> str:
    """
    created shifted string
    """
    new_s = "".join([
        chr((ord(x) + shift) % 255)
        for x in s
    ])
    return new_s


def iterate_over_shifts(s: str) -> Iterable[Tuple[str, int]]:
    """
    create generator to iterate over all possible shifts of given string
    """
    for shift in range(0, 255):
        yield make_shift(s, shift), shift


def compute_adequacy(s: str, word_base: List[str]) -> float:
    """
    compute score of given string adequacy, mode score -> more adequate is string
    """
    score = 0.0
    for word in s.lower().split(' '):
        if word in word_base:
            score += 1
    return score


def encrypt(s: str):
    # load dictionary
    words = open("words.txt", "r").read().split("\n")
    # create initial guess
    best_shift = (compute_adequacy(s, words), s, 0)

    # iterate over all possible variants
    for shifted_s, shift in iterate_over_shifts(s):
        # compute score for current variant
        current_score = compute_adequacy(shifted_s, words)
        # update answer if current variant is better then the old one
        if current_score > best_shift[0]:
            best_shift = (current_score, shifted_s, shift)

    print(f"best score (words found in dictionary) is {best_shift[0]}, shift is {255 - best_shift[2]}")
    print(f"and resulting string:\n{best_shift[1]}")


if __name__ == "__main__":
    input_line = input()
    encrypt(input_line)
