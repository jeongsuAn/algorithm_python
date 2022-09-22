class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = list(set(nums1)) #nums1의 중복을 제거
        nums2 = list(set(nums2))#nums2의 중복을 제거한후 sort
        nums2.sort()
       
        result = []
        
        for i in nums1:
            index = bisect.bisect_left(nums2,i) #이진 검색 및 들어가야할 자리에 target 값이 없으면 해당 index의 왼쪽을 리턴 
            if index < len(nums2) and nums2[index] == i:
                result.append(i)
        return result
        
        