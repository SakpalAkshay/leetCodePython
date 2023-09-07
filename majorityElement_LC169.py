class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dicts = {}
        for i in set(nums):
            dicts[i] = nums.count(i)
        size = len(nums)//2
        for index in dicts.keys():
            if dicts[index]>size:
                return index
