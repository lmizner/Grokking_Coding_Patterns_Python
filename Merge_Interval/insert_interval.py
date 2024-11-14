def insert_interval(existing_intervals, new_interval):
      
    # Pull the start and end values of the new interval
    new_start = new_interval[0]
    new_end = new_interval[1]

    # Set up empty list for output
    result = []

    # Initialize i at 0
    i = 0 
    
    # Merge Interval for inserting new interval 
    # Add existing intervals to result until we reach an opening for the new interval
    while i < len(existing_intervals) and existing_intervals[i][0] < new_start:
        result.append(existing_intervals[i])
        i += 1
    # Check if we need to add new interval first, or if an opening for new interval has occurred
    if not result or result[-1][1] < new_start:
        result.append(new_interval)
    # Otherwise merge intervals as needed
    else:
        result[-1][1] = max(result[-1][1], new_end)
    
    # Merge Interval for merging between results and existing intervals
    while i < len(existing_intervals):
        curr_start = existing_intervals[i][0]
        curr_end = existing_intervals[i][1]
        # Compare current start with result end
        # Add current interval to the end of results list
        if result[-1][1] < curr_start:
            result.append(existing_intervals[i])
        # Merge intervals with the end of results list
        else:
            result[-1][1] = max(result[-1][1], curr_end)
        i += 1
    
    return result


 


# Driver code
def main():

    test_cases = [
        ([[1, 2], [3, 4], [5, 8], [9, 15]], [2, 5]),
        ([[1, 3], [6, 9]], [2, 5]),
        ([[1, 2], [3, 4]], [5, 6]),
        ([[1, 5]], [2, 3]),
        ([[1, 2], [4, 5]], [2, 4]),
        ([[1, 2], [3, 5]], [2, 3]),
        ([[1, 5], [6, 8]], [4, 7]),
        ([[1, 3], [4, 5]], [2, 4]),
        ([[1, 10]], [5, 7])
    ]

    for i, (existing_intervals, new_interval) in enumerate(test_cases):
        print(f"{i + 1}. Existing Intervals: {existing_intervals}, New Interval: {new_interval}")
        merged_intervals = insert_interval(existing_intervals, new_interval)
        print(f"   Merged Intervals: {merged_intervals}")
        print("-" * 100)

if __name__ == '__main__':
    main()