class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start_idx = 0
        end_idx = len(nums)-1
        temp_idx = int((end_idx + start_idx)/2)
        while True :
            if nums[temp_idx] == target:
                return temp_idx
            elif nums[temp_idx] < target:
                start_idx = temp_idx+1
                temp_idx = int((end_idx + start_idx)/2)
            elif nums[temp_idx] > target:
                end_idx = temp_idx-1
                temp_idx = int((end_idx + start_idx)/2)
            if start_idx > end_idx:
                return -1
             