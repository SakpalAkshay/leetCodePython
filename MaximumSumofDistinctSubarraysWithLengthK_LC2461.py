class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        seen = collections.defaultdict(int)
        s = 0
        res = 0
        for i in range(k):
            s += nums[i]
            seen[nums[i]] += 1
        if len(seen) == k:
            res = s
        for i in range(k, len(nums)):
            s -= nums[i - k]
            s += nums[i]
            seen[nums[i - k]] -= 1
            if seen[nums[i - k]] == 0:
                del seen[nums[i - k]]
            seen[nums[i]] += 1
            if len(seen) == k:
                res = max(res, s)
        return res

   



