#!/usr/bin/python3
def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string
    and its first character.
    """
    # 1st. Calculates the length of the sentence
    length = len(sentence)

    # 2nd. Checks if the sentence is empty
    if length == 0:
        # If empty, the first character must be None
        first_char = None
    else:
        # If not empty, we can safely grab the first character
        first_char = sentence[0]

    # 3rd. Returns both values packed in a tuple
    return (length, first_char)
