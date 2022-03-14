'''
Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.
In case of multiple subarrays, return the subarray which comes first on moving from left to right.
Example 1:
Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements 
from 2nd position to 4th position 
is 12.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
'''

class Solution:
    def subArraySum(self,arr, n, s): 
        low = 0
        high = 0
        sum = 0
        Found = False
        if s in arr:
            Found = True
            val =  [arr.index(s)+1,arr.index(s)+1]
        while high<n and low>=0:
            if sum<s:
               sum+=arr[high]
               high+=1
            if sum>s:
                sum-=arr[low]
                low+=1

            if sum==s:
                if Found:
                    if val[0]>low+1:
                        return [low+1,high]
                    else:
                        return val
                else:
                    return [low+1,high]
                
        if Found:
            return val
        return [-1]

arr = [1,2,3,7,5]
n = len(arr)
s = 12
print(Solution().subArraySum(arr,n,s))

arr = [1,2,3,7,5]
n = len(arr)
s = 12
print(Solution().subArraySum(arr,n,s))

arr = [1,2,3,7,5]
n = len(arr)
s = 12
print(Solution().subArraySum(arr,n,s))