class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        sayiAdeti={}
        
        for curr in nums:  
            if curr in sayiAdeti:
                sayiAdeti[curr]+=1
            else:
                sayiAdeti[curr]=1
            
        for i in sayiAdeti.keys():
            if sayiAdeti[i]==1:
                return i
