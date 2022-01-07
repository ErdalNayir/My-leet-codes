class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        def merge(leftList,rightList):
            sortedArray=[]
            while len(leftList)>0 and len(rightList)>0:
                if leftList[0]>rightList[0]:
                    sortedArray.append(rightList[0])
                    rightList.remove(rightList[0])
                else:
                    sortedArray.append(leftList[0])
                    leftList.remove(leftList[0])

            while len(leftList)>0:
                sortedArray.append(leftList[0])
                leftList.remove(leftList[0])

            while len(rightList)>0:
                sortedArray.append(rightList[0])
                rightList.remove(rightList[0])


            return sortedArray


        def MergeSort(nums):
            if len(nums)<=1:
                return nums

            mid = len(nums) // 2

            left_list = MergeSort(nums[:mid])
            right_list = MergeSort(nums[mid:])

            return merge(left_list, right_list)

        squaredArray=[]
        for i in nums:
            i=(i)**2
            squaredArray.append(i)
        sortedSquared = MergeSort(squaredArray)
        return sortedSquared
