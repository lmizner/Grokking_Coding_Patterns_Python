def sort_colors(colors):
  
  # Initialize starting indices of pointers
  start = 0
  current = 0
  end = len(colors) - 1
  
  # End loop when current index becomes greater than end index
  while current <= end:
    # Swap start and current values
    if colors[current] == 0:
      colors[start], colors[current] = colors[current], colors[start]
      start += 1
      current += 1
    # No swap of values, continue to next iteration in the loop
    elif colors[current] == 1:
      current += 1
    # Swap end and current values
    else:
      colors[end], colors[current] = colors[current], colors[end]
      end -= 1

  return colors




# Driver code
def main():
    inputs = [[0, 1, 0], [1, 1, 0, 2], [2, 1, 1, 0, 0], [2, 2, 2, 0, 1, 0], [2, 1, 1, 0, 1, 0, 2]]

    # Iterate over the inputs and print the sorted array for each
    for i in range(len(inputs)):
        colors=inputs[i]
        print(i + 1, ".\tcolors:", colors)
        sort_colors(colors)
        print("\n\tThe sorted array is:", colors)
        print("-" * 100)

if __name__ == "__main__":
    main()