class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pivot = nums[0]
        vaild_pivot = 1
        nums_index = 1
        i = 0
        result = 1
        while i < len(nums):
            if pivot == nums[i]:
                if vaild_pivot == 0:
                    vaild_pivot = 1
                i += 1
            else :
                pivot = nums[i]
                vaild_pivot = 0
                nums[nums_index] = nums[i]
                nums_index += 1
                result += 1
                i += 1

        return result
