class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        if len(nums) == 1:
            result.append(nums[0])
            return result
        else:
            result.append(nums[0])
            for i in range(1,len(nums)):
                result.append(result[i-1]+nums[i])
            return result
                
            
            