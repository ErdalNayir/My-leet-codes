class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k==0 or len(nums)==1:
            nums[:]=nums
        elif k>len(nums):
            k=k%len(nums)
            nums[:]=nums[(-k):] + nums[:len(nums)-k]
        else:            
            nums[:]=nums[(-k):] + nums[:len(nums)-k]
