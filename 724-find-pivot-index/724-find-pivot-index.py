class Solution:
    def sumList(self, nums: List[int])->int:
        result = 0
        for i in range(len(nums)):
            result += nums[i]
        return result
        
        
    def pivotIndex(self, nums: List[int]) -> int:
        print(len(nums))
        leftSum = 0
        rightSum = self.sumList(nums[1:])
        for i in range(1,len(nums)):
            if leftSum == rightSum:
                return i-1
            leftSum+=nums[i-1]
            rightSum-=nums[i]
        if leftSum == rightSum:
            return len(nums)-1
        return -1
            