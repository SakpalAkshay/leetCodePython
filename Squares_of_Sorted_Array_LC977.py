class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square_val = [x*x for x in nums]
        square_val = sorted(square_val)
        return square_val
    
    def sortedSquares2(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        sortedArr = [0]* len(nums)
        index = right
        while left<=right:
            leftSquare = nums[left]*nums[left]
            rightSquare = nums[right]*nums[right]

            if rightSquare >= leftSquare :
                sortedArr[index] = rightSquare
                right -= 1
                index-=1
            else:
                sortedArr[index] = leftSquare
                left +=1
                index-=1
        return sortedArr
