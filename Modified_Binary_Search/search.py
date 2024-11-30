def search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        # Check if the target is at mid
        if arr[mid] == target:
            return True
        
        # Handle duplicates by shrinking the search space
        if arr[left] == arr[mid] == arr[right]:
            left += 1
            right -= 1
        # Left half is sorted
        elif arr[left] <= arr[mid]:
            # Check if target is in the left sorted portion
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            # Check if target is in the right sorted portion
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    # If target is not found
    return False



# Time Complexity = O(n)
# Space Complexity = O(1)



##################################################################



# Driver code
def test_search():
    test_cases = [
        ([47, 78, 90, 901, 10, 30, 40, 42, 42], 30, True),
        ([47, 78, 90, 901, 10, 30, 40, 42, 42], 100, False),
        ([4, 5, 6, 7, 0, 1, 2], 0, True),
        ([4, 5, 6, 7, 0, 1, 2], 3, False),
        ([1, 1, 3, 3, 3, 3, 1], 1, True),
        ([1, 1, 1, 3, 3, 3], 3, True),
        ([5, 6, 7, 1, 2, 3, 4], 6, True),
        ([5, 6, 7, 1, 2, 3, 4], 8, False),
        ([1], 1, True),
        ([2], 1, False)
    ]
    
    for i, (arr, target, expected) in enumerate(test_cases):
        result = search(arr, target)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed!")
        
# Run the test cases
test_search()