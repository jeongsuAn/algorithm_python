class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        dq = deque()  # 인덱스를 저장
        
        for i in range(len(nums)):
            # 1. 윈도우 범위를 벗어난 인덱스 제거
            while dq and dq[0] <= i - k:
                dq.popleft()
            
            # 2. 현재 요소보다 작은 요소들을 뒤에서 제거
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            # 3. 현재 인덱스 추가
            dq.append(i)
            
            # 4. 윈도우가 완성되면 결과 추가
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result