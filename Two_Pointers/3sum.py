def find_sum_of_three(nums, target):
  # Sort the array in ascending order
  nums.sort()
  
  # for loop will cycle through each index of nums for i 
  for i in range(0, len(nums)-2):
    # Pointers start positions must be defined inside for loop, so the reset at each loop
    pointer_1 = i + 1
    pointer_2 = len(nums) - 1
    # Ensure that each combo of values is tried without overlap of pointers
    while pointer_1 < pointer_2:
      # Calculate sum
      sum = nums[i] + nums[pointer_1] + nums[pointer_2]
      # If a match is found, return True
      if sum == target:
        return True
      # If we're less than target, increase pointer_1 value
      elif sum < target:
        pointer_1 += 1 
      # If we're greater than target, decrease pointer_2 value
      elif sum > target:
        pointer_2 -= 1
    # Iterate through i
    i += 1 
  # If no match found, return False
  return False



# Driver code
def main():
    nums_lists = [[3, 7, 1, 2, 8, 4, 5],
                  [-1, 2, 1, -4, 5, -3],
                  [2, 3, 4, 1, 7, 9],
                  [1, -1, 0],
                  [2, 4, 2, 7, 6, 3, 1]]

    targets = [10, 7, 20, -1, 8]

    for i in range(len(nums_lists)):
        print(i + 1, ".\tInput array: ", nums_lists[i], sep="")
        if find_sum_of_three(nums_lists[i], targets[i]):
            print("\tSum for", targets[i], "exists")
        else:
            print("\tSum for", targets[i], "does not exist")
        print("-"*100)

if __name__ == '__main__':
    main()
