def find_duplicate(nums):
  fast = slow = nums[0]
  
  while True:
    slow = nums[slow]
    fast = nums[nums[fast]]
    if slow == fast:
      break
    
  slow = nums[0]
   
  while slow != fast:
    slow = nums[slow]
    fast = nums[fast]
    
  return fast





# Driver code
def main():
    nums = [
        [1, 3, 2, 3, 5, 4], 
        [2, 4, 5, 4, 1, 3], 
        [1, 6, 3, 5, 1, 2, 7, 4], 
        [1, 2, 2, 4, 3], 
        [3, 1, 3, 5, 6, 4, 2]
    ]
    for i in range(len(nums)):
        print(i + 1, ".\tnums = ", nums[i], sep="")
        print("\tDuplicate number = ", find_duplicate(nums[i]), sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()