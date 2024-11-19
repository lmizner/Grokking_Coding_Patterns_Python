from heapq import *

class MedianOfStream:
    def __init__(self):

        # Heap to store small numbers (provides quick access to largest of small numbers)
        self.max_heap = []

        # Heap to store large numbers (provides quick access to smallest of large numbers)
        self.min_heap = []


    # This function should take a number and store it in the correct heap
    def insert_num(self, num):
        
        if not self.max_heap or -self.max_heap[0] >= num:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        # Make sure to maintain equal sized heaps (in case of odd numbers, difference of 1 is allowed)
        # Pop from max_heap and push to min_heap
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))

        # Pop from min_heap and push to max heap
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))


    # This function should return the median of the stored numbers
    def find_median(self):
        
        # If heaps are equal size, take the average of middle elements 
        if len(self.max_heap) == len(self.min_heap):
            
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
    
        # Otherwise, return top max_heap element
        return -self.max_heap[0]
            


# Time Complexity = O(1)
# Space Complexity = O(n)



###############################################################



# Driver code
def main():
    median_num = MedianOfStream()
    nums = [35, 22, 30, 25, 1]
    numlist = []
    x = 1
    for i in nums:
        numlist.append(i)
        print(x, ".\tData stream: ", numlist, sep="")
        median_num.insert_num(i)
        print("\tThe median for the given numbers is: " +
              str(median_num.find_median()), sep="")
        print(100*"-"+"\n")
        x += 1


if __name__ == "__main__":
    main()