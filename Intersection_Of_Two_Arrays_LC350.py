
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        exist = {}
        result = []
        if len(nums1) > len(nums2):
            for i in nums2:
                if i in exist:
                    exist[i]+=1
                else:
                    exist[i]=1
            
            for i in nums1:
                if i in exist and exist[i]!=0:
                    exist[i]-=1
                    result.append(i)
            

            
        else:
            for i in nums1:
                if i in exist:
                    exist[i]+=1
                else:
                    exist[i]=1

            for i in nums2:
                if i in exist and exist[i]!=0:
                    exist[i]-=1
                    result.append(i)
        return result
