class Solution:

    def searchInsert(self, nums: list, target: int) -> int:

        lo = 0
        hi = len(nums)
        mid = (lo+hi)//2
        
        if target<nums[0]:
            return 0
        if target>nums[-1]:
            return len(nums)
        if target ==nums[0]:
            return 0
        if target == nums[-1]:
            return hi-1
        else:
            while lo<hi:
                if mid==lo:
                    return mid+1
                
                elif mid==hi:
                    return mid-1

                elif nums[mid]>target:
                    hi = mid
                    mid = (lo+hi)//2
                    
                elif nums[mid]<target:
                    lo = mid
                    mid = (lo+hi)//2
                    
                elif nums[mid]==target:
                    return mid
                
                else:
                    if nums[mid]>target:
                        return mid-1
                    else:
                        return mid+1

nums = [1,3]
target = 3
print(Solution().searchInsert(nums,target))