def removeDuplicates(nums):

    i=0

    while i<(len(nums)-1):

        if nums[i]==nums[i+1]:

            nums.remove(nums[i])
        else:
            i=i+1

    return len(nums)














liste=[1,1,2,2,2,2,4,4,4]
print(liste)
removeDuplicates(liste)
print(liste)
