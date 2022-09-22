class Solution:
    def search_idx(self,nums:List[int])->int:
        left = 0
        right = len(nums) - 1
        while left <= right :
            mid = (left + right) // 2
            if nums[mid] >= nums[right]:
                left = mid+1
            elif nums[mid] < nums[right]:
                right = mid
        return right

    def search(self,nums:List[int],target:int) -> int:
        left = 0
        right = len(nums)-1
        rotation_idx = self.search_idx(nums)
        while left <= right:
            mid = (left+right)//2
            if nums[(mid+rotation_idx)%len(nums)] > target:
                right = mid-1
            elif nums[(mid+rotation_idx)%len(nums)] < target:
                left = mid+1
            else:
                return (mid+rotation_idx)%len(nums)
        return -1 # 만약 같은 겂이 없다면