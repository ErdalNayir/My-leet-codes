def searchInsert(nums, target):

    for i,j in enumerate(nums):

        if target == j:

            return i

    index =0

    for i in nums:

        if target>i:

            index+=1

    return index




print(searchInsert([1,3,4,5],2))
