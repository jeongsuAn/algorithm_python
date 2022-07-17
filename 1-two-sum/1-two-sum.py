class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num1Idx in range(len(nums)):
            num2 = target-nums[num1Idx]
            if target-nums[num1Idx] in nums:
                num2Idx = nums.index(num2)
                if num1Idx != num2Idx:
                    result = [num1Idx,num2Idx]
                    break
        return result
        