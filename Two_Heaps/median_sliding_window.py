from heapq import *

def median_sliding_window(nums, k):

    # To store medians
    medians = []

    # To track values to be removed from heaps
    outgoing_nums = {}

    # Max heap for small values and min heap for large values
    max_heap = []
    min_heap = []

    # Initialize max heap by multiplying each element by -1
    for i in range(k):
        heappush(max_heap, -1 * nums[i])

    # Tranfer top half of numbers from max to min heap (and update sign)
    for i in range(k // 2):
        element = heappop(max_heap)
        heappush(min_heap, -1 * element)

    # Variable to keep heaps balanced
    balance = 0

    i = k

    while True:

        # Check if the window size is odd
        if (k & 1) == 1:
            medians.append(float(max_heap[0] * -1))
        else:
            medians.append((float(max_heap[0] * -1) + float(min_heap[0])) * 0.5)

        # Break the loop if all elements have been processed
        if i >= len(nums):
            break

        # Set outgoing number
        out_num = nums[i - k]

        # Set incoming number
        in_num = nums[i]
        i += 1

        # If outgoing number is from max heap
        if out_num <= (max_heap[0] * -1):
            balance -= 1
        else:
            balance += 1

        # Add/update the outgoing number in the hash map
        if out_num in outgoing_nums:
            outgoing_nums[out_num] = outgoing_nums[out_num] + 1
        else:
            outgoing_nums[out_num] = 1

        # Check if the incoming number is less than the top of max heap
        if max_heap and in_num <= (max_heap[0] * -1):
            balance += 1
            heappush(max_heap, in_num * -1)
        # Otherwise, add to the min heap
        else:
            balance -= 1
            heappush(min_heap, in_num)

        # Rebalance the heaps
        if balance < 0:
            heappush(max_heap, (-1 * min_heap[0]))
            heappop(min_heap)
        elif balance > 0:
            heappush(min_heap, (-1 * max_heap[0]))
            heappop(max_heap)

        # Reset balance to zero
        balance = 0

        # Remove invalid numbers in hash map from top of max heap
        while(max_heap[0] * -1) in outgoing_nums and (outgoing_nums[max_heap[0] * -1] > 0):
            outgoing_nums[max_heap[0] * -1] = outgoing_nums[max_heap[0] * -1] - 1
            heappop(max_heap)

        # Remove invalid number in hash map from top of min heap
        while min_heap and min_heap[0] in outgoing_nums and (outgoing_nums[min_heap[0]] > 0):
            outgoing_nums[min_heap[0]] = outgoing_nums[min_heap[0]] - 1
            heappop(min_heap)

    return medians



# Time Complexity = O(nlogn)
# Space Complexity = O(n)



###############################################################



def main():
    input = (
            ([3, 1, 2, -1, 0, 5, 8],4), 
            ([1, 2], 1), 
            ([4, 7, 2, 21], 2), 
            ([22, 23, 24, 56, 76, 43, 121, 1, 2, 0, 0, 2, 3, 5], 5), 
            ([1, 1, 1, 1, 1], 2))
    x = 1
    for i in input:
        print(x, ".\tInput array: ", i[0],  ", k = ", i[1], sep = "")
        print("\tMedians: ", median_sliding_window(i[0], i[1]), sep = "")
        print(100*"-", "\n", sep = "")
        x += 1


if __name__ == "__main__":
    main()


