#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    Finds the biggest integer of a list without using max().
    """
    # 1st. Edge Case Check: If the list is empty, return None
    if not my_list:
        return None

    # 2nd. Set the initial record (biggest) to the first element
    biggest = my_list[0]

    # 3rd. Loops through every number in the list
    for number in my_list:
        # 4th. Comparison: If the current number breaks the record, update it
        if number > biggest:
            biggest = number

    # 5th. After the loop, returns the final biggest number found
    return biggest
