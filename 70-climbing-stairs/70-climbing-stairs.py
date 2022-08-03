class Solution:
    def climbStairs(self, n: int) -> int:
        step_before_i = 1
        step_i = 2
        if n == 1:
            return step_before_i
        elif n == 2:
            return step_i
        for i in range(n-2):
            temp = step_i+step_before_i
            step_before_i = step_i
            step_i = temp
        return step_i