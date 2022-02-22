class Solution:

    def pythagorean_triplets_exists(self,array:list) -> bool:
        """
        Input an array of numbers

        : returns:
        True : if there exists any pythagorean triplets
        False : if no pythagoreon triplets exists
        """

        if len(array)>2:
            array = sorted(array,reverse=True)
            array = [i**2 for i in array]
            last_elem = len(array)-1
            for i in range(0,last_elem-1):
                for j in range(i+1,last_elem):
                    if array[last_elem]+array[j]==array[i]:
                        return True
                last_elem-=1
            return False
        else:
            return False

array = [10, 4, 6, 12, 5]
Solution().pythagorean_triplets_exists(array)