class Solution:
    def rob(self, nums: List[int]) -> int:
        odd_sum = 0
        even_sum = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                odd_sum = max(odd_sum + nums[i], even_sum)
            else:
                even_sum = max(even_sum + nums[i], odd_sum)
        return max(odd_sum, even_sum)
        