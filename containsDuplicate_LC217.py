class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        orgLength = len(nums)
        setLength = len(set(nums))

        if(orgLength==setLength):
            return False
        
        return True
