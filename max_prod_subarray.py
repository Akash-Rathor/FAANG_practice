class Solution:

    def maxProduct(self, A):
        '''
        :: Input :  Takes a list of numbers

        :: Returns :  maximum possible product
        '''
        mi,ma = 1,1
        ans = A[0]
        for i in A:
            mi,ma = min(i,mi*i,ma*i),max(i,mi*i,ma*i)
            ans = max(ma,mi)
        return ans


A = [-4]
print(Solution().maxProduct(A))