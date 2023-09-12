class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        letMax = len(nums) 
        for i in range(letMax + 1):
            if i not in nums:
              return i
