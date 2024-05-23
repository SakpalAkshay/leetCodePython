class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square_val = [x*x for x in nums]
        square_val = sorted(square_val)
        return square_val
      
