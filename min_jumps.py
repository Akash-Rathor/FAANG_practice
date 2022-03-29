'''
Given an array of N integers arr[] where each element represents the max number of steps that can be made forward from that element.
Find the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then you cannot move through that element.
Note: Return -1 if you can't reach the end of the array.
'''

class Solution:
    def minJumps(self, arr, n):
    
    # x = arr[0]
        jumps = 0
        i = 0
        while i<=n-1:
            if arr[i]!=0:
                jumps+=1
                if i+arr[i]<n-1:
                    maxx = max(arr[i+1:i+arr[i]+1])
                    i += arr[i+1:i+arr[i]+1].index(maxx)+1
                else:
                    return jumps
            else:
                return -1

        return jumps

# arr = [0,1,1,1]
# arr = [1, 4, 3, 2, 6, 7]
# arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
arr = list(map(int,'9 10 1 2 3 4 8 0 0 8 0 0 0 0 1'.split()))
print(Solution().minJumps(arr,len(arr)))
