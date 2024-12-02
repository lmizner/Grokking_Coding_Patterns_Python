def get_bit(num, bit):

    temp = (1 << bit)
    temp = temp & num

    if temp == 0:
        return 0
    
    return 1



def find_all_subsets(nums):

    subsets = []

    if not nums:
        return [[]]
    
    else:
        subsets_count = 2 ** len(nums)

        for i in range(0, subsets_count):
            subset = set()

            for j in range(0, len(nums)):
                if get_bit(i, j) == 1 and nums[j] not in subset:
                    subset.add(nums[j])

            if i == 0:
                subsets.append([])
            
            else:
                subsets.append(list(subset))

    return subsets



# Time Complexity = O(2^n * n)
# Space Complexity = O(n)



#################################################################



def main():
    nums = [[], [2, 5, 7], [1, 2], [1, 2, 3, 4], [7, 3, 1, 5]]

    for i in range(len(nums)):
        print(i + 1, ". Set: ", nums[i], sep='')
        subsets = find_all_subsets(nums[i])
        print("   Subsets:", subsets)
        print("-"*100)


if __name__ == '__main__':
    main()


