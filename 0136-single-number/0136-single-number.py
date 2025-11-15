class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        stack = []
        result = nums[-1]
        i = 0
        for num in nums:
            if i % 2 == 0:
                stack.append(num)
                i += 1
            else: 
                prev_num = stack.pop()
                i += 1
                if num != prev_num:
                    result = prev_num
                    break
        return result