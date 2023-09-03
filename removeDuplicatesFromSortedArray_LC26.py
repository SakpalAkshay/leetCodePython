class Solution:
    # O(n^2) method
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i)>1:
                j = nums.count(i)
                while j > 1:
                    nums.remove(i)
                    j-=1
        return len(nums)

  #O(n) solution
  def removeDuplicatesTwo(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start != end:

            if nums[start]==nums[start+1]:
                nums.remove(nums[start+1])
                end = end - 1
            else:
                start = start + 1 
        return len(nums)
