class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        ifExist = set(nums1)
        result = []
        for i in nums2:
            if i in ifExist:
                result.append(i)
        
        if len(result) == 0:
            return -1
        else:
            return result[0]
