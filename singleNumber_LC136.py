class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        dicts = {}

        for i in set(nums):
            dicts[i] = nums.count(i)

        
        for i in dicts.keys():

            if dicts[i] == 1:
                return i

    def singleNumber2(self, nums: List[int]) -> int:
        
        #implementing count functionality to save time

        dicts ={}

        for i in nums:

            if i in dicts:
                dicts[i] += 1
            else:
                dicts[i] = 1

        
        for key, value in dicts.items():
            if value == 1:
                return key


