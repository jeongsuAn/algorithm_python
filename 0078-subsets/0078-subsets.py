class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = list()
        prev_elements = deque([])

        def dfs(elements):
            result.append(list(prev_elements))

            for e in elements:
                next_elements = elements[elements.index(e)+1:]

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return result