class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
       # any subarray that has maximum sum would eventually have max Average
       maximum = 0

       sum = 0 

       #sum of first k elements
       for i in range(k):
        sum = sum + nums[i]
       maximum = sum
       for j in range(k,len(nums)):
        sum = sum - nums[j-k] + nums[j]  
        maximum = max(sum,maximum)
       return maximum/k

            

