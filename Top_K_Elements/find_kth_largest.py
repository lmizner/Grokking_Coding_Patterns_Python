import heapq

def find_kth_largest(nums, k):

    # Initialize an empty list
    k_numbers_min_heap = []

    # Add first k elements to the list
    for i in range(k):
        k_numbers_min_heap.append(nums[i])

    # Convert list to min_heap
    heapq.heapify(k_numbers_min_heap)

    # Iterate through remaining elements in num array
    for i in range(k, len(nums)):

        # Compare current element with min heap element
        if nums[i] > k_numbers_min_heap[0]:
            
            # Remove smallest element
            heapq.heappop(k_numbers_min_heap)

            # Add current element
            heapq.heappush(k_numbers_min_heap, nums[i])
    
    return k_numbers_min_heap[0]



# Time Complexity = O((n-k)logk)
# Space Complexity = O(k)



############################################################################



# Driver code
def main():
    input_array = [
                    [1, 5, 12, 2, 11, 9, 7, 30, 20],
                    [5, 2, 9, -3, 7],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 4, 6, 0, 2],
                    [3, 5, 2, 3, 8, 5, 3]
                ]

    k = [3, 1, 9, 1, 4]

    for i in range(len(input_array)):
        print(i + 1, ".\tInput array: ", input_array[i], sep="")
        print("\tValue of k: ", k[i], sep="")
        print("\tkth largest number: ", find_kth_largest(input_array[i], k[i]), sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()



