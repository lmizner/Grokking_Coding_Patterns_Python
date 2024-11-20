# Template for array traversal
class traversal:
    def __init__(self):
        self.array = []
        
    def forward_traversal(self):
        for element in self.array:
            print(element)
        
    def backward_traversal(self):
        for i in range(len(self.array) - 1, -1, -1):
            print(self.array[i])



####################################################################



def merge_sorted(nums1, m, nums2, n):

    pointer_1 = m - 1
    pointer_2 = n - 1

    for p in range(n+m-1, -1, -1):
        if pointer_2 < 0:
            break
        if pointer_1 >= 0 and nums1[pointer_1] > nums2[pointer_2]:
            nums1[p] = nums1[pointer_1]
            pointer_1 -= 1
        else:
            nums1[p] = nums2[pointer_2]
            pointer_2 -= 1
            
    return nums1



# Time Complexity = O(n+m)
# Space Complexity = O(1)



####################################################################



# Driver code
def main():
    m = [9, 2, 3, 1, 8]
    n = [6, 1, 4, 2, 1]
    nums1 = [[23, 33, 35, 41, 44, 47, 56, 91, 105, 0, 0, 0, 0, 0, 0], [1, 2, 0], [1, 1, 1, 0, 0, 0, 0], [6, 0, 0], [12, 34, 45, 56, 67, 78, 89, 99, 0]]
    nums2 = [[32, 49, 50, 51, 61, 99], [7], [1, 2, 3, 4], [-99, -45], [100]]
    k = 1
    for i in range(len(m)):
        print(k, ".\tnums1: ", nums1[i], ", m: ", m[i], sep = "")
        print("\tnums2: ", nums2[i], ", n: ", n[i], sep = "")
        print("\n\tMerged list: ", merge_sorted(nums1[i], m[i], nums2[i], n[i]), sep = "")
        print("-"*100, "\n")
        k += 1


if __name__ == "__main__":
    main()


