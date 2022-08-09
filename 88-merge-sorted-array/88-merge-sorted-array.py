class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        temp_len = 0
        nums1_index = 0
        nums2_index = 0
        if m == 0:
            for i in range(len(nums2)):
                nums1[i] = nums2[i]
            return
        elif n == 0:
            return
        else:
            temp_array = []
            while temp_len < n+m:
                if nums1[nums1_index] >= nums2[nums2_index]:
                    temp_array.append(nums2[nums2_index])
                    nums2_index+=1
                    if nums2_index == n :
                        while nums1_index!=m:
                            temp_array.append(nums1[nums1_index])
                            nums1_index+=1
                        for i in range(len(temp_array)):
                            nums1[i] = temp_array[i]
                        return
                else:
                    temp_array.append(nums1[nums1_index])
                    nums1_index+=1
                    if nums1_index == m :
                        while nums2_index!=n:
                            temp_array.append(nums2[nums2_index])
                            nums2_index+=1
                        for i in range(len(temp_array)):
                            nums1[i] = temp_array[i]
                        return
