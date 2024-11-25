from collections import defaultdict
import heapq


def third_max(nums): 

    # Initialize empty min heap
    heap = []

    # Initialize set to track numbers added to heap
    taken = set()

    # Iterate through input list
    for index in range(len(nums)):

        # Skip number if already in the set (duplicate)
        if nums[index] in taken:
            continue
        
        # If heap already contains 3 numbers
        if len(heap) == 3:

            if heap[0] < nums[index]:

                # Remove smallest number from heap and set
                taken.remove(heap[0])
                heapq.heappop(heap)

                # Add current larger number to heap and set
                heapq.heappush(heap, nums[index])
                taken.add(nums[index])

        # If hepa has fewer than 3 numbers
        else:
            heapq.heappush(heap, nums[index])
            taken.add(nums[index])


    # Handle cases with fewer than 3 distinct numbers
    # Only one distinct number
    if len(heap) == 1:
        return heap[0]
    
    # Only two distinct numbers, return larger of the two
    elif len(heap) == 2:
        first_num = heap[0]
        heapq.heappop(heap)
        return max(first_num, heap[0])
    
    # If there are 3 distinct numbers
    return heap[0]



# Time Complexity = O(n)
# Space Complexity = O(1)



############################################################################



# Driver code
def main():
    test_cases = [
        [3, 2, 1],
        [1, 2],
        [2, 2, 3, 1],
        [5, 5, 4, 3, 2],
        [1, 1, 1, 1]
    ]

    i = 0
    for nums in test_cases:
        print(i + 1, ".\tnums: ", nums, sep="")
        print("\n\tThe third maximum is: ", third_max(nums), sep="")
        print("-" * 100)
        i += 1

if __name__ == "__main__":
    main()


