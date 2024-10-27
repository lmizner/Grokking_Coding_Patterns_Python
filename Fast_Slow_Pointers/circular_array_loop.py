def circular_array_loop(nums):
    size = len(nums)
    
    for i in range(size):
        slow = fast = i
        forward = nums[i] > 0
      
        while True:
            slow = next_step(slow, nums[slow], size) 
            if is_not_cycle(nums, forward, slow):
                break
        
            fast = next_step(fast, nums[fast], size)
            if is_not_cycle(nums, forward, fast):
                break
            
            fast = next_step(fast, nums[fast], size)
            if is_not_cycle(nums, forward, fast):
                break
        
            if slow == fast:
                return True
                
    return False

# A function to calculate the next step
def next_step(pointer, value, size):
    result = (pointer + value) % size
    if result < 0:
        result += size
    return result

# A function to detect a cycle doesn't exist
def is_not_cycle(nums, prev_direction, pointer):

        curr_direction = nums[pointer] >= 0
        if (prev_direction != curr_direction) or (abs(nums[pointer] % len(nums)) == 0):
            return True
        else:
            return False

# Driver code
def main():

    input = (
            [-2, -3, -9],
            [-5, -4, -3, -2, -1],
            [-1, -2, -3, -4, -5],
            [2, 1, -1, -2],
            [-1, -2, -3, -4, -5, 6],
            [1, 2, -3, 3, 4, 7, 1],
            [2, 2, 2, 7, 2, -1, 2, -1, -1]
            )
    num = 1

    for i in input:
        print(f"{num}.\tCircular array = {i}")
        print(f"\n\tFound loop = {circular_array_loop(i)}")
        print("-"*100, "\n")
        num += 1


if __name__ == "__main__":
    main()