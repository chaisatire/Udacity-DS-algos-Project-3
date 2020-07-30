def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    # Corner cases for square root
    if number == 0:
        return 0
    if number == 1:
        return 1
    if number < 0:
        return 'Please provide a positive number'

    # Defining the initial start and end for recursive function
    begin = 0
    end = number

    # Here we will call the recursive function to find the square root.
    return findSqrt(number, begin, end)


def findSqrt(number, begin, end):
    """ Support Function:
    This is a recursive function which used binary search and aims to find the square root of the number. 
    The time complexity is O(logn) as we are using Binary Search as well recursion.
    Space complexity is O(1) as we are working on given input.
    """

    # Defining the termination condition when the number has a float instead of integer as it's square root
    if begin == end:
        return begin - 1

    # creating a pivot to potentially eliminate half of the numbers
    pivot = (begin + end) // 2

    square = pivot * pivot

    if square == number:
        return pivot
    elif square < number:
        return findSqrt(number, pivot + 1, end)
    else:
        return findSqrt(number, begin, pivot)


# Test case 1
print("Pass" if  (4 == sqrt(16)) else "Fail")

# Test case 2:
print("Pass" if  (5 == sqrt(27)) else "Fail")

# Test case 3:
print("Pass" if  (0 == sqrt(0)) else "Fail")
print("Pass" if  (1 == sqrt(1)) else "Fail")

# Test case 4:  Edge case of negative number
print("Pass" if  ('Please provide a positive number' == sqrt(-1)) else "Fail")
