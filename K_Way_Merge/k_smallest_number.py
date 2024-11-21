from heapq import *

def k_smallest_number(lists, k):

    # Initialize mini-heap to track smallest elements
    k_smallest = []

    # Loop through list elements
    for i in range(len(lists)):
        
        # If there are no elements in the input list, continue to the next iteration
        if len(lists[i]) == 0:
            continue
        # Place first element on each list in the min-heap
        else:
            heappush(k_smallest, (lists[i][0], i, 0))


    numbers_checked = 0
    smallest_number = 0

    # Iterate of min-heap elements
    while k_smallest:
        
        # Pull smallest number, list index, and number indedx from top of heap
        smallest_number, list_index, num_index = heappop(k_smallest)
        numbers_checked += 1

        if numbers_checked == k:
            break

        # If more elements in list of top element, add next element to min-heap
        if num_index + 1 < len(lists[list_index]):
            heappush(k_smallest, (lists[list_index][num_index + 1], list_index, num_index + 1))

    # Return kth number
    return smallest_number



# Time Complexity = O(mlogm + klogm)
# Space Complexity = O(m)



####################################################################



# Driver code
def main():
    # multiple inputs for efficient results
    lists = [[[2, 6, 8], [3,6,10], [5, 8, 11]],
             [[1, 2, 3], [4, 5], [6, 7, 8, 15], [10, 11, 12, 13], [5, 10]],
             [[], [], []],
             [[1, 1, 3, 8], [5, 5, 7, 9], [3, 5, 8, 12]],
             [[5, 8, 9, 17], [], [8, 17, 23, 24]]]

    k = [5, 50, 7, 4, 8]

    # loop to execute till the length of list k
    for i in range(len(k)):
        print(i + 1, ".\t Input lists: ", lists[i],
              f"\n\t K = {k[i]}",
              f"\n\t {k[i]}th smallest number from the given lists is: ",
              k_smallest_number(lists[i], k[i]), sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()

    