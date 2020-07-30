def search_index_binary(input_list, number, start, end):
    """
    This is a recursive helper function. It aims to find the index of the number.
    This function is using Binary Search to find out the index.
    If index doesn't exist then we get -1 as the output.

    The time complexity is O(logn) as we are using Binary Search.
    Space complexity is O(1) as we are working on given input.
    """
    # Termination condition if index is not found.
    if start > end:
        return -1

    mid_index = (start + end) // 2
    mid_element = input_list[mid_index]

    # Termination condition if index is found
    if mid_element == number:
        return mid_index

    left_index = search_index_binary(input_list, number, start, mid_index - 1)
    right_index = search_index_binary(input_list, number, mid_index + 1, end)

    # At the end of the function if element doesn't exist on either left or right side then we get -1
    # As there are no duplicates on 1 side we should get -1 and on other side we get the index.
    # Using the max function we are returning the index if it exists.
    return max(left_index, right_index)


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # Edge case when either list is empty or number is None
    if input_list == None or number == None:
        return -1

    start = 0
    end = len(input_list) - 1

    # Calling the recursive helper function
    return search_index_binary(input_list, number, start, end)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


# Test case 1
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

# Test case 2 - non rotated array
test_function([[1, 2, 3, 4], 3])

# Test Case 3 - Edge case 1
test_function([[], 6])

# Test case 4 - Edge case 2
test_function([[], None])

