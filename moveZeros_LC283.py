class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i == 0:
                nums.remove(i)
                nums.append(0)
    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0

        for fast in range(len(nums)):

            if nums[fast] !=0 and nums[slow]==0:
                nums[fast] , nums[slow] = nums[slow], nums[fast]
                #we swap
            
            if nums[slow]!=0:
                slow +=1
