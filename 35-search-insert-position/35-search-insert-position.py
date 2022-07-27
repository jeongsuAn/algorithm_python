class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        index = int((end + start) / 2)
        while True:
            if start>end:
                return start
            if nums[index]>target:
                if index== 0 :
                    return 0
                if start == end :
                    return index
                end = index-1
                index = int((end + start) / 2)
            elif nums[index]<target:
                if start == end :
                    return index+1
                start = index+1
                index = int((end + start) / 2)
            elif nums[index] == target:
                return index
