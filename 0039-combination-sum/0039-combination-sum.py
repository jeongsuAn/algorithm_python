from collections import deque
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = list()
        prev_elements = deque()
        candidates.sort()

        def dfs(current_sum:int, prev_elements:deque, start_index:int):
            if current_sum == target:
                result.append(list(prev_elements))
                return

            if current_sum > target:
                return

            for i in candidates[start_index:]:
                if target-current_sum >= i >= candidates[0]:
                    prev_elements.append(i)
                    dfs(current_sum + i, prev_elements, candidates.index(i))
                    prev_elements.pop()

        dfs(0, prev_elements, 0)
        return result
