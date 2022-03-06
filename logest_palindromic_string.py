class Solution:

    def LPS(self,string:str) ->str:

        if len(string)<2:
            return len(string)
        start=0
        maxLength = 1
        for i in range(len(string)):
            low = i-1
            high = i+1
            while high < len(string) and string[high]==string[i]:
                high+=1
            while low>0 and string[low]==string[i]:
                low-=1

            while low >= 0 and high < len(string) and string[low]==string[high]:
                low-=1
                high+=1

            length = high - low - 1
            if (maxLength < length):
                maxLength = length
                start=low+1

        print(string[start:start + maxLength])

        return maxLength

string='abbac'
print(Solution().LPS(string))