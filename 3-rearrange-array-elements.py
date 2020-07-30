class MaxHeap:
    """ Support Class
    From the examples given and the time complexity defined I choose MaxHeap as algorithm.
    The examples point that the Output is always in descending order of elements given e.g. [964, 852]

    The overall time complexity is O(nlogn) because heapifying the arrays takes O(nlogn) time compleixty.
    Space complexity for is O(n)
    """
    def __init__(self, initial_size=10):
        self.cbt = [None for _ in range(initial_size)]
        self.next_index = 0

    def size(self):
        return self.next_index

    def is_empty(self):
        return self.size() == 0

    def remove(self):
        if self.size() == 0:
            return None
        self.next_index -= 1

        to_remove = self.cbt[0]
        last_element = self.cbt[self.next_index]

        # place last element of the cbt at the root
        self.cbt[0] = last_element

        # we do not remove the elementm, rather we allow next `insert` operation to overwrite it
        self.cbt[self.next_index] = to_remove
        self._down_heapify()
        return to_remove

    def insert(self, data):
        # insert element at the next index
        self.cbt[self.next_index] = data

        # heapify
        self._up_heapify()

        # increase index by 1
        self.next_index += 1

        # double the array and copy elements if next_index goes out of array bounds
        if self.next_index >= len(self.cbt):
            temp = self.cbt
            self.cbt = [None for _ in range(2 * len(self.cbt))]

            for index in range(self.next_index):
                self.cbt[index] = temp[index]

    def _up_heapify(self):
        child_index = self.next_index

        while child_index >= 1:
            parent_index = (child_index - 1) // 2
            parent_element = self.cbt[parent_index]
            child_element = self.cbt[child_index]

            if parent_element < child_element:
                self.cbt[parent_index] = child_element
                self.cbt[child_index] = parent_element
                child_index = parent_index
            else:
                break

    def _down_heapify(self):
        parent_index = 0

        while parent_index < self.next_index:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2

            parent = self.cbt[parent_index]
            left_child = None
            right_child = None

            max_element = parent

            # check if left child exists
            if left_child_index < self.next_index:
                left_child = self.cbt[left_child_index]

            # check if right child exists
            if right_child_index < self.next_index:
                right_child = self.cbt[right_child_index]

            # compare with left child
            if left_child is not None:
                max_element = max(parent, left_child)

            # compare with right child
            if right_child is not None:
                max_element = max(right_child, max_element)

            # check if parent is rightly placed
            if max_element == parent:
                return

            if max_element == left_child:
                self.cbt[left_child_index] = parent
                self.cbt[parent_index] = max_element
                parent = left_child_index

            elif max_element == right_child:
                self.cbt[right_child_index] = parent
                self.cbt[parent_index] = max_element
                parent = right_child_index

    def get_minimum(self):
        # Returns the minimum element present in the heap
        if self.size() == 0:
            return None
        return self.cbt[0]


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) == 0:
        return [None]

    max_heap = MaxHeap()

    # Creating the max heap
    for element in input_list:
        max_heap.insert(element)

    number_1 = ""
    number_2 = ""

    # Fetching the numbers out of Max Heap
    for i in range(max_heap.size()):
        if i % 2 == 1:
            number_1 += str(max_heap.remove())
        else:
            number_2 += str(max_heap.remove())
    return [int(number_1), int(number_2)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]

    if output == [None] and solution == [None]:
        print("pass")
        return
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# Test case 1:
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

# Test case 2: Repeating Number
test_function([[1, 1, 2, 2, 3, 3], [321, 321]])

# Test case 3: Empty list
test_function([[], [None]])