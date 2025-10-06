def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j - 1

        array[j+1] = key

    return array

def test_insertion_sort():
    # Test case 1: Empty array
    assert insertion_sort([]) == [], "Test failed for empty array"
    
    # Test case 2: Single element array
    assert insertion_sort([5]) == [5], "Test failed for single element array"
    
    # Test case 3: Already sorted array
    assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Test failed for already sorted array"
    
    # Test case 4: Reverse sorted array
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5], "Test failed for reverse sorted array"
    
    # Test case 5: Array with duplicates
    assert insertion_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9], "Test failed for array with duplicates"
    
    # Test case 6: Array with negative numbers
    assert insertion_sort([-5, 0, -3, 8, -1, 2]) == [-5, -3, -1, 0, 2, 8], "Test failed for array with negative numbers"
    
    # Test case 7: Large array
    test_array = list(range(1000, 0, -1))  # Create a large reverse sorted array
    assert insertion_sort(test_array) == list(range(1, 1001)), "Test failed for large array"
    
    print("All test cases passed!")

# Run the test function
test_insertion_sort()
