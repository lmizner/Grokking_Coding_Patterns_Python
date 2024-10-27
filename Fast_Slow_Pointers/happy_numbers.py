def is_happy_number(n):
  
  # Define function to calculate sum of the squared digits
  def sum_of_square_digits(num):
    total_sum = 0
    for digit in str(num):
      total_sum += int(digit)**2
    return total_sum
    
  # Initialize slow and fast pointers  
  slow_pointer = n 
  fast_pointer = sum_of_square_digits(n)
  
  # Continue incrementally moving pointers until we've found a cycle or a happy number
  while fast_pointer != 1 and slow_pointer != fast_pointer:
    slow_pointer = sum_of_square_digits(slow_pointer)
    fast_pointer = sum_of_square_digits(sum_of_square_digits(fast_pointer))
    
  # Verify if result is a happy number or not  
  if fast_pointer == 1:
    return True
  
  return False




def main():
    inputs = [1, 5, 19, 25, 7]
    for i in range(len(inputs)):
        print(i+1, ".\tInput Number: ", inputs[i], sep="")
        print("\n\tIs it a happy number? ", is_happy_number(inputs[i]))
        print("-" * 100)


if __name__ == '__main__':
    main()

    