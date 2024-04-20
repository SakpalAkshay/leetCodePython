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

    
    
    def findMaxAverage1(self, nums: List[int], k: int) -> float:
        cur_sum = 0
        res = float('-inf')

        l = r = 0

        while r < len(nums):
            cur_sum += nums[r]

            if r - l + 1 == k:
                res = max(res, cur_sum)
                cur_sum -= nums[l]
                l += 1
            
            r += 1
        
        return res / k


