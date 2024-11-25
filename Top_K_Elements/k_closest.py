import heapq

class Point:
    # __init__ will be used to make a Point type object
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # __lt__ is used for max-heap
    def __lt__(self, other):
        return self.distance_from_origin() > other.distance_from_origin()

    # __str__ is used to print the x and y values
    def __str__(self):
        return '[{self.x}, {self.y}]'.format(self=self)

    # distance_from_origin calculates the distance using x, y coordinates
    def distance_from_origin(self):
        # ignoring sqrt to calculate the distance
        return (self.x * self.x) + (self.y * self.y)

    __repr__ = __str__



############################################################################



def k_closest(points, k):
  
    points_max_heap = []

    # Put first k points in max_heap
    for i in range(k):
        heapq.heappush(points_max_heap, points[i])

    # Iterate through remaining points
    for i in range(k, len(points)):

        # If closer to origin, remove top point from heap and add point
        if points[i].distance_from_origin() < points_max_heap[0].distance_from_origin():
                heapq.heappop(points_max_heap)
                heapq.heappush(points_max_heap, points[i])

    return list(points_max_heap)


# Helper Function
def lst_to_str(lst):
    out = "["
    for i in range(len(lst)-1):
        out += str(lst[i]) + ", "
    out += str(lst[len(lst)-1]) + "]"
    return out



# Time Complexity = O(nlogk)
# Space Complexity = O(k)



############################################################################



# Driver code
def main():
    points_one = [Point(1, 3), Point(3, 4), Point(2, -1)]
    points_two = [Point(1, 3), Point(2, 4), Point(2, -1), Point(-2, 2),
        Point(5, 3), Point(3, -2)]
    points_three = [Point(1, 3), Point(5, 3), Point(3, -2), Point(-2, 2)]
    points_four = [Point(2, -1), Point(-2, 2), Point(1, 3), Point(2, 4)]
    points_five = [Point(1, 3), Point(2, 4), Point(2, -1), Point(-2, 2), 
        Point(5, 3), Point(3, -2), Point(5, 3), Point(3, -2)]

    k_list = [2, 3, 1, 4, 5]
    points = [points_one, points_two, points_three, points_four, points_five]

    for i in range(len(k_list)):
        result = k_closest(points[i], k_list[i])
        print(i + 1, ".\tSet of points: ", sep="", end='')
        print(lst_to_str(points[i]))
        print("\tk:", k_list[i])
        print("\tHere are the k =", k_list[i], "points closest to the", \
        "origin (0, 0): ", end='')
        print(lst_to_str(result))
        print("-"*100)

if __name__ == '__main__':
    main()





