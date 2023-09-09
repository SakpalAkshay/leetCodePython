'''Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.'''


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        start = 0
        end = len(nums) - 1

        if len(nums)==0:
            return 0
        elif len(nums)==1:
            if target == nums[0]:
                return 0
            elif target>nums[0]:
                return 1
            else:
                return 0    
        else:

            while start < end:

                mid = (start + end)//2

                if nums[mid]==target:
                    return mid
            
                elif target > nums[end]:
                    return end + 1
            
                elif target < nums[start]:
                    return start
                
                elif target == nums[end]:
                    return end 
            
                elif target == nums[start]:
                    return start
            
                elif target > nums[mid] and target<nums[mid+1]:
                    return mid + 1
                elif target < nums[mid] and target>nums[mid-1]:
                    return mid 
            
                elif target>nums[mid]:
                    start = mid + 1
                else:
                    end = mid -1 
            

            

