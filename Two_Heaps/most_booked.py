import heapq

def most_booked(meetings, rooms):
    
    # Count array to track the number of meetings each room holds
    count = [0] * rooms

    # Creat min_heaps for available and used rooms
    available = [i for i in range(rooms)]
    used = []

    # Sort the meeting by start time
    meetings.sort()

    # Cycle through all meetings by start and end time
    for start_time, end_time in meetings:
        # Free up rooms that aren't used during current start time
        while used and used[0][0] <= start_time:
            ending, room = heapq.heappop(used)
            heapq.heappush(available, room)

        # If no rooms are available, delay meetings until one is
        if not available:
            end, room = heapq.heappop(used)
            end_time = end + (end_time - start_time)
            heapq.heappush(available, room)

        # Assign meeting to room with lowest number
        room = heapq.heappop(available)
        heapq.heappush(used, (end_time, room))
        count[room] += 1

    # Return the room that held the most meetings
    return count.index(max(count))



# Time Complexity = O(mlogm + mlogn)
# Space Complexity = O(n)



###############################################################



# Driver code
def main():
    meetings = [[[0,10],[1,11],[2,12],[3,13],[4,14],[5,15]],
				[[1,20],[2,10],[3,5],[4,9],[6,8]],
				[[1, 2], [0, 10], [2, 3], [3, 4]],
				[[0, 2], [1, 2], [3, 4], [2, 4]],
				[[1, 9], [2, 8], [3, 7], [4, 6], [5, 11]]]
    rooms = [3, 3, 2, 4, 3]

    for i in range(len(meetings)):
        print(i+1, '.', '\tMeetings: ', meetings[i], sep='')
        print('\tRooms: ', rooms[i], sep='')
        booked_rooms = most_booked(meetings[i], rooms[i])
        print('\n\tRoom that held the most meetings: ', booked_rooms)
        print('-' * 100)

if __name__ == '__main__':
    main()

