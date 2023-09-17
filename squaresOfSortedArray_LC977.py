class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = []
        for i in nums:
            l.append(i*i)

        return sorted(l)

    def sortedSquares2(self, nums: List[int]) -> List[int]:
        low = 0 
        high = len(nums) - 1
        sortedSq = []
        while low <= high:

            if abs(nums[low]) > nums[high]:
                sortedSq.append(nums[low]*nums[low])
                low+=1
            else:
                sortedSq.append(nums[high]*nums[high])
                high -=1
        
        return sortedSq[::-1]
