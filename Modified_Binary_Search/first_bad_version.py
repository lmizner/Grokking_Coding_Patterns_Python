# # -- DO NOT CHANGE THIS SECTION -----------------
    
# import main as api_call

# def is_bad_version(v): # is_bad_version() is the API function that returns true or false depending upon whether the provided version ID is bad or not
#     return api_call.is_bad(v)
# # ----------------------------------------------- 

def is_bad_version(s):
    return s >= v

def first_bad_version(n):

    first = 1 
    last = n
    calls = 0

    while first <= last:
        mid = first + (last - first) // 2

        if is_bad_version(mid):
            last = mid - 1

        else:
            first = mid + 1
        
        calls += 1
    
    return [first, calls]



# Time Complexity = O(logn)
# Space Complexity = O(1)



##################################################################



# Driver code
def main():
    global v
    test_case_versions = [38, 13, 29, 40, 23]
    first_bad_versions = [28, 10, 10, 28, 19]

    for i in range(len(test_case_versions)):
        v = first_bad_versions[i]
        if i > 0:
            print()
        print(i + 1,  ".\tNumber of versions: ", test_case_versions[i], sep="")
        result = first_bad_version(test_case_versions[i])
        print("\n\tFirst bad version: ",
              result[0], ". Found in ", result[1], " API calls.", sep="")
        print("-"*100)


if __name__ == '__main__':
    main()


