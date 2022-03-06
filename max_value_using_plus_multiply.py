'''
Given a string of numbers, the task is to find the maximum value from the string, you can add a ‘+’ or ‘*’ sign between any two numbers.
Examples: 
 

Input : 01231
Output : 
((((0 + 1) + 2) * 3) + 1) = 10
In above manner, we get the maximum value i.e. 10
'''

class Solutions:

    def max_val(self,string:str) ->int:
        '''
        input : string of numbers 

        ::returns:

        maximum value out of those numbers using '+' and '*' operators
        '''

        max_val = int(string[0])
        for i in string[1:]:
            if(i in '01' or max_val < 2):
                max_val += int(i)
            else:
                max_val *= int(i)

        return max_val


if __name__ == '__main__':
    print(Solutions().max_val('01891'))
        