def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """

    """
    The algorithm uses several pointers to traverse the array only once. 
    We are keeping track of 3 values i.e. current index and where next 0 & 2 will be added.
    The values are swapped during traversal.
    """
    index_zero = 0  # Zero should be the first element
    current_index = 0  
    index_two = len(input_list) - 1 # Two should be the last element

    # Continue to loop while index of 1 is less than bottom index of 2
    while current_index <= index_two:

        # If current value is 0 then just increment index of 0.
        # Also increment the current_index.
        if input_list[current_index] == 0:
            input_list[current_index], input_list[index_zero] = input_list[index_zero], input_list[current_index]
            index_zero += 1
            current_index += 1
            
        # If the value at current_index is already 1 then nothing to do and increment the start index
        elif input_list[current_index] == 1:
            current_index += 1
        
        # If value at current index is 2 then we need to push it to the end.
        elif input_list[current_index] == 2:
            input_list[current_index], input_list[index_two] = input_list[index_two], input_list[current_index]
            index_two -= 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# Test case 1:
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# Test case 2: Only 0's and 1's
test_function([0, 1, 1, 0, 0, 1])

# Test case 3: Only 1 element
test_function([0, 0, 0, 0])

# Test case 4: Empty list
test_function([])