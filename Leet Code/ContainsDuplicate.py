def containsDuplicate(self, nums: List[int]) -> bool:
        NewList=set()
        for i in range(len(nums)):      
            NewList.add(nums[i])
        if len(nums) != len(NewList):
            return True
        return False
