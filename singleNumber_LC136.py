class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        dicts = {}

        for i in set(nums):
            dicts[i] = nums.count(i)

        
        for i in dicts.keys():

            if dicts[i] == 1:
                return i

