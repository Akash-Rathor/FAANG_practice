'''
The cumulative sum of an array at index i is defined as the sum of all elements of the array from index 0 to index i.
example 1
Initial Array: [1, -2, 3, 4, -6]
Cumulative Sum: [1, -1, 2, 6, 0]

example 2
Initial Array: [1, 2, 3, 4]
Cumulative Sum: [1, 3, 6, 10]
'''

class Solution:
    def getCumulativeSum(self, arr:list) ->list:
        '''
        input : array
        returns : Cumulative summed array
        time complexity :  O(N)
        space complexity : O(1)
        '''
        sum = 0
        for i in range(len(arr)):
            sum+=arr[i]
            arr[i]=sum
        
        return arr

    def getCumulativePositiveSum(self, arr:list) ->list:
        '''
        input : array
        returns : Cumulative array of positive numbers only
        time complexity :  O(N)
        space complexity : O(N)
        '''
        sum = 0
        array =[]
        for i in range(len(arr)):
            sum+=arr[i]
            if sum>0:
                array.append(sum)
            
        return array

arr = [1, 2, 3, 4]
print(Solution().getCumulativeSum(arr))
arr = [1, -2, 3, 4, -6]
print(Solution().getCumulativePositiveSum(arr))