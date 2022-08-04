class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_len = len(nums)/2
        num_dictionary = {}
        for i in range(len(nums)):
            if nums[i] in num_dictionary:
                num_dictionary[nums[i]] = num_dictionary[nums[i]]+1
                if num_dictionary[nums[i]] > max_len:
                    return nums[i]
            else:
                num_dictionary[nums[i]] = 1
                if num_dictionary[nums[i]] > max_len:
                    return nums[i]
