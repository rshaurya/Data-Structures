# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array

# using dictionary
def missingNum_dict(nums):
    d = {}
    res = None
    for i in range(1, len(nums) + 1):
        d[i] = 0
    for i in nums:
        d[i] = 1
    for i, j in d.items():
        if j == 0:
            res = i

    return res

# print(missingNum_dict([0,1,3]))

# using list
def missingNum(nums):
    res = None
    track = [0] * (len(nums) + 1)
    for i in nums:
        track[i] = 1
    for i in range(1, len(nums) + 1):
        if track[i] == 0:
            res = i
    
    return res

print(missingNum([0,1,3,1,5]))
