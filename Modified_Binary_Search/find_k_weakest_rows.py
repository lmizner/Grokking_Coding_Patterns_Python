import heapq

def find_k_weakest_rows(matrix, k):

    # Get the number of rows and columns in matrix
    m = len(matrix)
    n = len(matrix[0])

    # Helper function to perform binary search on each row
    def binary_search(row):

        low = 0
        high = n

        while low < high:
            mid = low + (high - low) // 2

            if row[mid] == 1:
                low = mid + 1
            else:
                high = mid
        
        return low
    
    # Priority queue (min-heap) to store k weakest rows
    pq = []

    for i, row in enumerate(matrix):
        strength = binary_search(row)
        entry = (-strength, -i)

        # Add row to heap
        if len(pq) < k or entry > pq[0]:
            heapq.heappush(pq, entry)
        
        # Remove strongest row from heap
        if len(pq) > k:
            heapq.heappop(pq)

    # Extract the k weakest rows from the heap
    indexes = []

    while pq:
        strength, i = heapq.heappop(pq)
        indexes.append(-i)

    # Reverse order from weakest to strongest
    indexes = indexes[::-1]
    return indexes



# Time Complexity = O(mlognk)
# Space Complexity = O(k)



##################################################################



def main():
    matrix_list = [
        [[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]],
        [[1, 1, 0, 0], [1, 0, 0, 0], [1, 1, 1, 1], [1, 1, 0, 0]],
        [[1, 1], [1, 1], [0, 0], [1, 0], [1, 1]],
        [[1, 0, 0, 0], [1, 1, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0]],
        [[1, 0, 0], [0, 0, 0], [1, 1, 1], [1, 1, 0]]
    ]
    k_values = [2, 3, 3, 2, 1]

    for i in range(len(matrix_list)):
        print(f"{i + 1}.\tInput matrix: \n\tmatrix = {matrix_list[i]}\n\tk = {k_values[i]}")
        weakest_rows = find_k_weakest_rows(matrix_list[i], k_values[i])
        print(f"\n\tIndexes of the {k_values[i]} weakest rows: {weakest_rows}")
        print("-" * 100)

if __name__ == '__main__':
    main()
