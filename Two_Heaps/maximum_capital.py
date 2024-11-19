from heapq import heappush, heappop

def maximum_capital(c, k, capitals, profits):

    # Initialize a min_heap 
    capitals_min_heap = []

    # Insert all capitals values into min_heap
    for i in range(len(capitals)):
        heappush(capitals_min_heap, (capitals[i], i))

    # Track current capital and initialize max_heap
    current_capital = c
    profits_max_heap = []

    # Calculate capital of all required number of projects, containing max profit 
    for _ in range(k):

        # Select projects and push to max_heap
        while capitals_min_heap and capitals_min_heap[0][0] <= current_capital:
            # Pop from capitals min heap
            c, i = heappop(capitals_min_heap)

            # Push to profits max heap (using negated element)
            heappush(profits_max_heap, (-profits[i]))

        # Check if max_heap is empty
        if not profits_max_heap:
            break

        # Select projects from max_heap with max profit
        # Pop from max heap
        max_profit = -heappop(profits_max_heap)
        
        # Update current capital by adding project, max profit element
        current_capital += max_profit

    return current_capital



# Time Complexity = O(nlogn)
# Space Complexity = O(n)



###############################################################



# Driver Code
def print_capitals_min_heap(capitals):
    arr = []
    for i in range(len(capitals)):
        arr.append(capitals[i])
        print("\t", arr)


def main():
    input = (
              (0, 1, [1, 1, 2], [1 ,2, 3]),
              (1, 2, [1, 2, 2, 3], [2, 4, 6, 8]),
              (2, 3, [1, 3, 4, 5, 6], [1, 2, 3, 4, 5]),
              (1, 3, [1, 2, 3, 4], [1, 3, 5, 7]),
              (7, 2, [6, 7, 8, 10], [4, 8, 12, 14]),
              (2, 4, [2, 3, 5, 6, 8, 12], [1, 2, 5, 6, 8, 9])
            )
    num = 1
    for i in input:
        print(f"{num}.\tProject capital requirements:  {i[2]}")
        print(f"\tProject expected profits:      {i[3]}")
        print(f"\tNumber of projects:            {i[1]}")
        print(f"\tStart-up capital:              {i[0]}")
        print("\n\tMaximum capital earned: ",
              maximum_capital(i[0], i[1], i[2], i[3]))
        print("-" * 100, "\n")
        num += 1


if __name__ == "__main__":
    main()

