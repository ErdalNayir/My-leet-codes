def reverseWords(num):
    if num==0:
        return num

    lowerLimit=num//10

    while((lowerLimit*lowerLimit)<=num): #Lower point
        lowerLimit=lowerLimit+1

    lowerLimit=lowerLimit-1

    return lowerLimit
