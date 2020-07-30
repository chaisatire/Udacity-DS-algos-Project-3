import random

def get_min_max(ints):
    """
    Return a tuple(smallest, largest) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    # Defining Edge conditions
    if ints is None or len(ints) == 0:
        return None

    smallest = ints[0]
    largest = ints[0]

    # Iterating through all the elements to find the smallest and largest values.
    for i in range(1, len(ints)):
        if ints[i] < smallest:
            smallest = ints[i]
        if ints[i] > largest:
            largest = ints[i]
    return smallest, largest


# Test case 1
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print('\n')

# Test case 2: list with negative numbers
l = [i for i in range(-24, 30)]
random.shuffle(l)

print("Pass" if ((-24, 29) == get_min_max(l)) else "Fail")
print('\n')

# Test case 3: List with only 1 element
l = [i for i in range(1, 2)]
random.shuffle(l)

print("Pass" if ((1, 1) == get_min_max(l)) else "Fail")
print('\n')

# Test case 4: Empty list
l = []

print("Pass" if (None == get_min_max(l)) else "Fail")
