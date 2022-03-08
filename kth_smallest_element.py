'''
Find the kth smallest element from the array
expected time complexity O(N)
'''

class Solution:
    def kthSmallest(self,arr, l, r, k):
        b=max(arr)
        p=[0 for i in range(b)]
        for i in arr:
            p[i-1]=i
        r=[]
        for i in range(len(p)):
            if p[i]!=0:
                r.append(p[i])
                
        return(r[k-1])


arr = [7,10,4,20,15]
l = 0
r = len(arr)
k = 4
print(Solution().kthSmallest(arr,l,r,k))