import heapq

class KthLargest:
    # Constructor to initialize heap and add values in it
    def __init__(self, k, nums):
        
        self.top_k_heap = []
        self.k = k

        for element in nums:
            self.add(element)
            


    # Adds element in the heap and return the Kth largest
    def add(self, val):
        
        if len(self.top_k_heap) < self.k:
            heapq.heappush(self.top_k_heap, val)

        elif val > self.top_k_heap[0]:
            heapq.heappop(self.top_k_heap)
            heapq.heappush(self.top_k_heap, val)
        
        return self.top_k_heap[0]


# Time Complexity = O(logk)
# Space Complexity = O(K)



############################################################################



# Driver code
def main():
    nums = [3, 6, 9, 10]
    temp = [3, 6, 9, 10]
    print("Initial stream: ", nums, sep = "")
    print("k: ", 3, sep = "")
    k_largest = KthLargest(3, nums)
    val = [4, 7, 10, 8, 15]
    for i in range(len(val)):
        print("\tAdding a new number ", val[i], " to the stream", sep = "")
        temp.append(val[i])
        print("\tNumber stream: ", temp, sep = "")
        print("\tKth largest element in the stream: ", k_largest.add(val[i]))
        print("-"*100)

if __name__ == "__main__":
    main()


