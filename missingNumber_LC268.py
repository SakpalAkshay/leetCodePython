class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        letMax = len(nums) 
        for i in range(letMax + 1):
            if i not in nums:
              return i

    def missingNumber2(self, nums: List[int]) -> int:
        inputSum = 0 
        for i in nums:
            inputSum+=i
        outSum = 0
        for i in range(len(nums)+1):
            outSum+=i

        return outSum - inputSum
