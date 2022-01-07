def BinarySearch(Numlist, target):
    firstIndex=0
    lastIndex=len(Numlist)-1

    middleIndex = firstIndex+(lastIndex - firstIndex)/2
    middleIndex=int(round(middleIndex))

    while(firstIndex<=lastIndex):

        if Numlist[middleIndex]<target:
            firstIndex=middleIndex+1
            middleIndex = firstIndex+(lastIndex - firstIndex)/2
            middleIndex=int(round(middleIndex))
        elif Numlist[middleIndex]>target:
            lastIndex=middleIndex-1
            middleIndex = firstIndex+(lastIndex - firstIndex)/2
            middleIndex=int(round(middleIndex))
        else:
            return Numlist[middleIndex]

    return -1


Nums=[10,13,18,19,23,27,29,35,37,42,44,49,50,57,58,66,73,75,79,83]
print(BinarySearch(Nums,10))
