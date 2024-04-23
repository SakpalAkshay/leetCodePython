class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
   
    def removeElement2(self, nums: List[int], val: int) -> int:

        #Handling Few Edge Cases 
        
        if len(nums)==0:
            return 0
        
        if len(nums)==1 and nums[0]==val:
            return 0

        if len(nums)==1 and nums[0]!=val:
            return 1

        # After Edge Cases 
        i =0
        j = len(nums) - 1

        while i<=j:
            if nums[j]==val:
                j-=1
                continue
            elif nums[i]==val:
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
            else:
                i+=1

        return j + 1


    #Pushed more simple solution
    def removeElement3(self, nums: List[int], val: int) -> int:
         l = 0
         for r in range(len(nums)):
            if nums[r] != val:  # loop through if num[r] if not equals then swap else just r gets incremented whenever it matches, 
                nums[l] = nums[r]
                l+=1
         return l
