from collections import deque

# Function to clean up the deque
def clean_up(i, current_window, nums):
    while current_window and nums[i] >= nums[current_window[-1]]:
        current_window.pop()

# Function to find the maximum in all possible windows
def find_max_sliding_window(nums, w):
    # If the list contains only one element, it is the max by default
    if len(nums) == 1:
        return nums
    
    output = []
    current_window = deque()

    # Loop through window values for first window
    for i in range(w):
        clean_up(i, current_window, nums)
        current_window.append(i)

    # Append largest value in the window to the output
    output.append(nums[current_window[0]])

    # Loop through window values for all windows following the first
    for i in range(w, len(nums)):
        clean_up(i, current_window, nums)

        # Slide window
        if current_window and current_window[0] <= (i - w):
            current_window.popleft()

        # Append largest value in window to output
        current_window.append(i)
        output.append(nums[current_window[0]])

    # Return largest window values
    return output



# driver code
def main():
    window_sizes = [3, 3, 3, 3, 2, 4, 3, 2, 3, 6]
    nums_list = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [1, 5, 8, 10, 10, 10, 12, 14, 15, 19, 19, 19, 17, 14, 13, 12, 12, 12, 14, 18, 22, 26, 26, 26, 28, 29, 30],
        [10, 6, 9, -3, 23, -1, 34, 56, 67, -1, -4, -8, -2, 9, 10, 34, 67],
        [4, 5, 6, 1, 2, 3],
        [9, 5, 3, 1, 6, 3],
        [2, 4, 6, 8, 10, 12, 14, 16],
        [-1, -1, -2, -4, -6, -7],
        [4, 4, 4, 4, 4, 4]
    ]

    for i in range(len(nums_list)):
        print(f"{i + 1}.\tInput list:\t{nums_list[i]}")
        print(f"\tWindow size:\t{window_sizes[i]}")
        output = find_max_sliding_window(nums_list[i], window_sizes[i])
        print(f"\n\tMaximum in each sliding window:\t{output}")
        print("-"*100)

if __name__ == '__main__':
    main()