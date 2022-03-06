'''A message containing letters from A-Z is being encoded to numbers using the following mapping:

 'A' -> 1
 'B' -> 2
 ...
 'Z' -> 26
Given an encoded message A containing digits, determine the total number of ways to decode it modulo 109 + 7.
'''

class Solution:

    def numDecodings(self,string):
        '''
        input: A string

        ::return : 

        int: a number of ways a string can decode
        '''
        number_of_ways = 0
        if '0' not in string:
            number_of_ways+=1
        for i in range(0,len(string)-1):
            j=i+1
            if int(string[i]+string[j]) in range(10,27):
                number_of_ways += 1

        return number_of_ways

print(Solution().numDecodings(string='12'))