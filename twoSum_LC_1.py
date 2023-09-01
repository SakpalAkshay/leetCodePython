'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.'''


#o(n^2) solution 
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):

                if (nums[i]+ nums[j] == target):
                    return [i,j]

    #o(n) solution
    def twoSum2(self,nums, target):
        seen_values = {}
        
        for index, value in enumerate(nums):
            if target - value in seen_values:
                return seen_values[target - value], index
            
            else:
                seen_values[value] = index
                
        return -1
