class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        LastMaxSum=-1000000
        currentMaxSum=0

        for i in nums:
            currentMaxSum=currentMaxSum+i
            if(LastMaxSum < currentMaxSum):
                LastMaxSum = currentMaxSum
            if(currentMaxSum < 0):
                currentMaxSum = 0

        return LastMaxSum
        
