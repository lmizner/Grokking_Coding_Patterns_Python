def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        if array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1



##################################################################



def single_non_duplicate(nums): 

    # Initialize left and right pointers
    left = 0
    right = len(nums) - 1

    while left != right:
        
        # Calculate the midpoint of the array
        middle = left + (right - left) // 2

        # If mid-point is odd, decrement to make it even
        if middle % 2 != 0:
            middle -= 1

        # If middle and middle + 1 are the same, then single element after mid-point
        if nums[middle] == nums[middle + 1]:
            left = middle + 2

        # Otherwise search for single element before mid-point
        else:
            right = middle

    # Return single element value
    return nums[left]



# Time Complexity = O(logn)
# Space Complexity = O(1)



##################################################################



# Driver code
def main():

    nums = [[1, 2, 2, 3, 3, 4, 4], [1, 1, 2, 2, 3, 4, 4, 5, 5], [1, 1, 2, 3, 3], [1, 1, 2], [0, 2, 2, 3, 3, 4, 4, 5, 5]]

    for i in range(len(nums)):
        print(str(i + 1) + ".\tThe Array = ", nums[i] , sep = "")
        print("\tSingle Element Found: ", single_non_duplicate(nums[i]), sep = "")
        print("-" * 100)

if __name__ == '__main__':
    main()



