class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxCount = 0
        for i in nums:
            if i == 0:
                count = 0 
            else:
                count+=1
                maxCount = max(maxCount, count)
            
        return maxCount
