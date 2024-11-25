import heapq

class Solution:
    def min_cost_to_hire_workers(self, quality, wage, k):

        # Create list of tuples with wage/quality ratio 
        workers = sorted([(w/q, q) for w, q in zip(wage, quality)])

        # Initialize max heap
        heap = []

        # Sum of qualities of selected workers
        total_quality = 0

        # Initialize minimum cost
        min_cost = float('inf')

        # Iterate through workers sorted by wage-to-quality ratio
        for ratio, q in workers:

            # Add worker quality to heap
            heapq.heappush(heap, -q)
            total_quality += q

            # More than k workers, remove largest quality
            if len(heap) > k:
                total_quality += heapq.heappop(heap)

            # Exactly k workers, calculate cost
            if len(heap) == k:
                min_cost = min(min_cost, ratio * total_quality)

        return min_cost



# Time Complexity = O(nlogk)
# Space Complexity = O(k)



############################################################################



# Driver code
def main():
    qualities = [
        [10, 20, 5],
        [3, 1, 10, 10, 1],
        [4, 5, 6],
        [2, 3, 1],
        [10, 10, 10]
    ]
    
    wages = [
        [70, 50, 30],
        [4, 8, 2, 2, 7],
        [8, 10, 12],
        [5, 6, 2],
        [50, 60, 70]
    ]
    
    k_values = [2, 3, 2, 2, 2]
    sol = Solution()
    for i in range(len(qualities)):
        print(i+1, ".\tqualities:", qualities[i])
        print("\twages:", wages[i])
        print("\tk:", k_values[i])
        result = sol.min_cost_to_hire_workers(qualities[i], wages[i], k_values[i])
        print("\n\tMinimum cost to hire", k_values[i], "workers =", result)
        print("-"*100)

if __name__ == "__main__":
    main()

