def removeElement(nums,val):

    nums[:] = (num for num in nums if num!=val)

    return len(nums)





liste=[0,1,2,2,3,0,4,2]

print(liste)
print(removeElement(liste,2))
print(" ")
print(liste)
