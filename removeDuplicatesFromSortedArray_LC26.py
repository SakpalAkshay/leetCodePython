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

  # Another O(n^2) solution using Two pointers
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
# Pushed O(n) solution
 def removeDuplicatesThree(self, nums: List[int]) -> int:
        # let there be two pointer one tracking the unique elements place
        j = 1
        
        for i in range(1,len(nums)):
            if nums[i] !=nums[i-1]:
                nums[j] = nums[i]
                j+=1
        return j
#using while loop
def removeDuplicates4(arr)-> int:
    # arr = [2,3,3,3,4,5,6,6,9,9] op = [2,3,4,5,6,9]
    #because it is sorted but duplicate then 0th index <= 1st index and so on
    #because its required Inplace you either swap or you replace element with something else
    i = 1 
    j = 1 #as we required to return unique elements in the start we need to return the start of array as unique element and to track it we use j
    while i < len(arr):
        if arr[i] == arr[i-1]:
            i+=1
            continue
        else:
            #we found a unique element
            arr[j] = arr[i]
            j +=1
        i+=1
    return j

