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
    return left



##################################################################



def find_closest_elements(nums, k, target):

    # Check if length of nums is same as k
    if len(nums) == k:
        return nums
    
    # Check if target is less than or equal to first element of nums
    if target <= nums[0]:
        return nums[0:k]
    
    # Check if target is greater than or equal to last element of nums
    if target >= nums[-1]:
        return nums[len(nums) - k: len(nums)]
    
    # Find first closest element to target using binary search
    first_closest = binary_search(nums, target)

    # Initialize sliding window pointers
    window_left = first_closest - 1
    window_right = window_left + 1

    # Expand sliding window until equal to k
    while (window_right - window_left -1) < k:

        # Move window right
        if window_left == -1:
            window_right += 1
            continue

        # Move window left
        if window_right == len(nums) or abs(nums[window_left] - target) <= abs(nums[window_right] - target):
            window_left -= 1

        # Move window right
        else:
            window_right += 1

    # Return k closest elements
    return nums[window_left + 1 : window_right]



# Time Complexity = O(logn + k)
# Space Complexity = O(1)



##################################################################



# Driver code
def main():

    nums = [
                [1, 2, 3, 5, 6, 7,8],
                [1, 2, 3, 4, 5],
                [1, 2, 4, 5, 6],
                [1, 2, 3, 4, 5, 10]
                ]
    k = [4, 4, 2, 3]
    num = [4, 3, 10, -5]
    for i in range(len(nums)):
        print((i + 1), ".\tThe ", k[i],
              " Closest Elements for the number ", num[i], " in the array ",
              nums[i], " are:", sep="")
        print("\t", find_closest_elements(nums[i], k[i], num[i]))
        print("-" * 100)

if __name__ == '__main__':
    main()

