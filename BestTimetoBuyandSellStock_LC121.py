class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #we will use a Two Pointer approach
        l = 0
        r = 1
        maxProfit = 0
        while r < len(prices):
            #profit can be negative too because we would only be taking the max of it
            currentProfit = prices[r] - prices[l]

            #we would only update our profit if left value is smaller than right

            if prices[l] < prices[r]:
                maxProfit = max(currentProfit, maxProfit)

            else:# we move left to rights position we found something that is much less than our current minimum stock
                l = r
            
            r+=1 #increament to get to next prices
        return maxProfit
        
