class Solution:

    def __init__(self,array):
        self.array = array

    def KlargestUnique(self,n:int) ->list:
        """
        input a number of items to get
        output: list of n Unique largest numbers
        
        : Returns :
            list: list of k number of largest elements from the input list
        """
        array = sorted(self.array,reverse=True)
        if len(array)>0:
            temp = [array[0]]
            for i in array[1:]:
                if len(temp)<n:
                    if i==temp[-1]:
                        pass
                    else:
                        temp.append(i)
            return temp
        else:
            return array
                
    def Klargest(self,n:int) ->list:
        '''
        input a number of items to get
        output: list of n largest numbers
        '''
        array = sorted(self.array,reverse=True)
        if len(array)>0:
            return array[0:n]
        else:
            return array
                


array = [1,5,4,2,7,7,7,7]
print(Solution(array = array).Klargest(n=4))
print(Solution(array = array).KlargestUnique(n=4))