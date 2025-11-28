#!/usr/bin/python3
"""Module 1-my_list: defines class MyList that inherits from list"""

class MyList(list):
    """MyList inherits from list and adds print_sorted method"""

    def print_sorted(self):
        """Print the list in ascending order without modifying the original list.

        >>> my_list = MyList()
        >>> my_list.append(3)
        >>> my_list.append(1)
        >>> my_list.append(2)
        >>> my_list.print_sorted()
        [1, 2, 3]
        >>> my_list
        [3, 1, 2]
        """
        print(sorted(self))
