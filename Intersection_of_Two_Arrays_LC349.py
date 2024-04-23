class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)

        return list(s1.intersection(s2))

    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        exist = {}
        result = []
        for i in nums1:
            if i not in exist:
                exist[i] = 1
        
        for j in nums2:
            if j in exist and exist[j]==1:
                result.append(j)
                exist[j]+=1
        return result
