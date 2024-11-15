import heapq

def find_sets(intervals):
    
    # If no intervals have been given
    if not intervals:
        return 0
    
    # Step 1: Sort the meetings in increasing order of start time
    intervals.sort(key = lambda x: x[0])
    
    # Step 2: Initialize min-heap to store end times of meetings
    heap = []

    # Step 3: Add the first meeting and 1 room
    heapq.heappush(heap, intervals[0][1])

    # Step 4: Process all remaining meetings
    for i in intervals[1:]:
        # If the romm with the earliest end time is free, resuse it
        if heap[0] <= i[0]:
            heapq.heappop(heap)

        # Add the current meeting end time to the heap
        heapq.heappush(heap, i[1])

    # Return the total number of rooms required (size of heap)
    return len(heap)




# Driver code with multiple test cases

test_cases = [
    [[2,8],[3,4],[3,9],[5,11],[8,20],[11,15]],
    [[1,3],[2,6],[8,10],[9,15],[12,14]],
    [[1,2],[4,6],[3,4],[7,8]],
    [[1,7],[2,6],[3,7],[4,8],[5,8]],
    [[1,2],[1,2],[1,2]]
]

# Testing the function with all test cases
for i, intervals in enumerate(test_cases, 1):
    print(f"Test case {i}:")
    print(f"Intervals: {intervals}")
    print(f"Minimum number of meeting rooms required: {find_sets(intervals)}\n")



