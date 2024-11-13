def min_sub_array_len(target, nums):
    # Initialize window_size with positive infinity
    window_size = float('inf')
    # Initialize start and sum with 0
    start = 0
    sum = 0
    # Iterate over the input array
    for end in range(len(nums)):
        sum += nums[end]
        # Remove elements from the start of the window while sum is greater than target
        while sum >= target:
            # Find size of current window
            curr_subarr_size = (end + 1) - start
            window_size = min(window_size, curr_subarr_size)
            # Remove element from the start of the window
            sum -= nums[start]
            start += 1

    if window_size != float('inf'):
        return window_size

    return 0


# Driver code
def main():
    target = [7, 4, 11, 10, 5, 15]
    input_arr = [[2, 3, 1, 2, 4, 3], [1, 4, 4], [1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 2, 3, 4], [1, 2, 1, 3], [5, 4, 9, 8, 11, 3, 7, 12, 15, 44]]
    for i in range(len(input_arr)):
        window_size = min_sub_array_len(target[i], input_arr[i])
        print(i+1, ".\t Input array: ", input_arr[i],"\n\t Target: ", target[i],
            "\n\t Minimum Length of Subarray: ", window_size, sep="")
        print("-"*100)


if __name__ == "__main__":
    main()