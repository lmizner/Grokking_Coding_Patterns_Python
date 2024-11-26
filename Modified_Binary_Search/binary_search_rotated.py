def binary_search_rotated(nums, target):

    low = 0
    high = len(nums) - 1

    while low <= high:

        # Calculate midpoint of list
        mid = low + (high - low) // 2

        # Check if target is at midpoint
        if nums[mid] == target:
            return mid
        
        # Check if target is less than midpoint
        if nums[low] <= nums[mid]:
            if nums[low] <= target and target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        
        # Check if target is greater than midpoint
        else:
            if nums[mid] < target and target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    
    # If target is not in list
    return -1



# Time Complexity = O(logn)
# Space Complexity = O(1)



##################################################################



def main():
    nums_list = [[5, 6, 7, 1, 2, 3, 4],
                 [40, 50, 60, 10, 20, 30],
                 [47, 58, 69, 72, 83, 94, 12, 24, 35], 
                 [77, 82, 99, 105, 5, 13, 28, 41, 56, 63], 
                 [48, 52, 57, 62, 68, 72, 5, 7, 12, 17, 21, 28, 33, 37, 41]]

    target_list = [1, 50, 12, 56, 5]

    for i in range(len(target_list)):
        print((i + 1), ".\tRotated array: ", nums_list[i], "\n\ttarget", target_list[i], "found at index ", \
              binary_search_rotated(nums_list[i], target_list[i]))
        print("-"*100)


if __name__ == '__main__':
    main()

