class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]: 
        
        firstIndex=0
        lastIndex=len(numbers)-1

        while firstIndex!=lastIndex:

            if numbers[firstIndex]+numbers[lastIndex]>target:
                lastIndex=lastIndex-1
            elif numbers[firstIndex]+numbers[lastIndex]<target:
                firstIndex=firstIndex+1
            else:
                return [firstIndex+1,lastIndex+1]
