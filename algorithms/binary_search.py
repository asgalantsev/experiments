def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if(arr[mid] == x):
            return mid
        elif arr[mid]> x:
            return binary_search(arr, low, mid-1, x)
        else:
            return binary_search(arr, mid+1, high, x)
    
    return -1

# Test cases
def test_binary_search():
    # Test when element is present
    arr = [2, 3, 4, 10, 40]
    x = 10
    assert binary_search(arr, 0, len(arr)-1, x) == 3

    # Test when element is not present
    arr = [2, 3, 4, 10, 40]
    x = 5
    assert binary_search(arr, 0, len(arr)-1, x) == -1

    # Test with single element array
    arr = [5]
    x = 5
    assert binary_search(arr, 0, len(arr)-1, x) == 0

    # Test with empty array
    arr = []
    x = 5
    assert binary_search(arr, 0, len(arr)-1, x) == -1

    # Test when element is first in array
    arr = [2, 3, 4, 10, 40]
    x = 2
    assert binary_search(arr, 0, len(arr)-1, x) == 0

    # Test when element is last in array
    arr = [2, 3, 4, 10, 40]
    x = 40
    assert binary_search(arr, 0, len(arr)-1, x) == 4

    # Test with odd length array
    arr = [1, 3, 5, 7, 9]
    x = 5
    assert binary_search(arr, 0, len(arr)-1, x) == 2

    # Test with even length array
    arr = [1, 3, 5, 7, 9, 11]
    x = 7
    assert binary_search(arr, 0, len(arr)-1, x) == 3

    # Test with large array
    arr = list(range(1000000))
    x = 500000
    assert binary_search(arr, 0, len(arr)-1, x) == 500000

    print("All test cases passed!")

# Run test cases
test_binary_search()

