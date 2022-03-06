'''
Given two sorted arrays arr1[] of size N and arr2[] of size M.
Each array is sorted in non-decreasing order. Merge the two arrays into one sorted array in non-decreasing order
without using any extra space.
'''

class Solution:
    def merge(self, arr1, arr2, n, m):
        if n<=m:
            shortest_len=n
            large = m
        else:
            shortest_len=m
            large = n
        i=j=0
        while len(arr1)<n+m and i<len(arr1):
            temp = arr1[i]
            if temp>=arr2[j]:
                arr1.insert(i,arr2[j])
                arr2.pop(j)
                i+=1
            else:
                i+=1
        arr2 = arr1[shortest_len+1:]+arr2
        arr1 = arr1[:shortest_len+1]

        return arr1,arr2

arr1 = [7,10]
arr2 = list(map(int,"2 2 6 6 7 7 10 11 12 14 15 16".split()))
n,m =len(arr1)-1,len(arr2)-1
print(Solution().merge(arr1, arr2, n, m))