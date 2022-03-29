'''
Sort an array of 0s,1s and 2s in O(N) time and O(1) space complexity
'''

class Solution:
    def sort012(self,arr,n):
        '''
        input : array of 0s,1s and 2s
        
        returns: Sorted array
        '''
        i=0
        count2 = 0
        for i in arr:
            if i==2:
                count2+=1

        while i<n-count2:

            if arr[i]==0:
                arr.pop(i)
                arr.insert(0,0)
                i+=1

            elif arr[i]==2:
                arr.append(2)
                arr.pop(i)

            elif arr[i]==1:
                i+=1
        

        return arr


arr = [0,2,1,2,0,1,1,1,1,1,1,1,2,2,2,2,2,2,2,0,1,0,0,0,0,0,0]
print(Solution().sort012(arr,n=len(arr)))