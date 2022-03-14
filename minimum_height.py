class Solution:
    def getMinDiff(self, arr, n, k):
        mini=minimum = min(arr)
        def max_min(maxi,mini):
            if mini-k>0:
                mini-=k
            else:
                mini+=k
            maxi = max(arr)
            return mini,maxi
        mini,maxi = max_min(min(arr),max(arr))
        if maxi-k>0 and maxi-mini<=0:
            max_min(min(arr),maxi-k)
        if mini-k>0 and maxi-mini<=0:
            max_min(mini+k,maxi-k)

        return maxi-mini


arr = [2,6,3,4,7,2,10,3,2,1]
n = 10
k = 5
print(Solution().getMinDiff(arr,n,k))