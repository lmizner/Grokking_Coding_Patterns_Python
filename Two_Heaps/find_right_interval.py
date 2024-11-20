import heapq

def find_right_interval(intervals):

    # Initialize result array
    result = [-1] * len(intervals)

    # Initialize min_heaps for start and end points
    start_heap = []
    end_heap = []

    # Populate heaps with intervals
    for i, interval in enumerate(intervals):
        heapq.heappush(start_heap, (interval[0], i))
        heapq.heappush(end_heap, (interval[1], i))

    # Process each interval based on its end point
    while end_heap:

        # Get the interval with the smallest end point
        value, index = heapq.heappop(end_heap)

        # Remove all start points from that are smaller than current end point
        while start_heap and start_heap[0][0] < value:
            heapq.heappop(start_heap)

        # If start heap is not empty, top element is smallest valid interval
        if start_heap:
            result[index] = start_heap[0][1]

    # Return result list
    return result



# Time Complexity = O(nlogn)
# Space Complexity = O(n)



###############################################################



def main():
    test_cases = [
        [[1, 2]],
        [[3, 4], [2, 3], [1, 2]],
        [[1, 4], [2, 3], [3, 4]],
        [[5, 6], [1, 2], [3, 4]],
        [[1, 3], [2, 4], [3, 5], [4, 6]],
    ]

    for i, test_case in enumerate(test_cases):
        print(i + 1, "\tintervals:", test_case)
        result = find_right_interval(test_case)
        print("\n\tOutput:", result)
        print("-" * 100)

if __name__ == "__main__":
    main()