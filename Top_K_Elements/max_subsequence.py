import heapq

def max_subsequence(nums, k):
  
    # Initialize min heap
    min_heap = []

    # Iterate through list of numbers
    for i, num in enumerate(nums):
        
        # Push to heap
        heapq.heappush(min_heap, (num, i))

        # Maintain the size of heap to k
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # Extract elements from heap and sort in orginal order
    result = sorted(min_heap, key = lambda x: x[1])
    return [x[0] for x in result]



# Time Complexity = O(nlogk)
# Space Complexity = O(k)



############################################################################



def main():
    test_cases = [
        ([3, 4, 3, 3], 2),
        ([2, 1, 3, 3], 2),
        ([-1, -2, 3, 4], 3),
        ([1, 2, 3, 4, 5], 3),
        ([9, -1, -3, 8, 7], 2)
    ]
    
    for i, (nums, k) in enumerate(test_cases, 1):
        print(f"{i}\tnums = {nums}, k = {k}")
        result = max_subsequence(nums, k)
        print(f"\n\tResult: {result}\n")
        print("-"*100)
if __name__ == "__main__":
    main()

