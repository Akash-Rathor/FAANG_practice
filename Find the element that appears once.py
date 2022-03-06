'''Given an array where every element occurs three times, except one element which occurs only once.
Find the element that occurs once. The expected time complexity is O(n) and O(1) extra space. 
'''

class Solution:

    def appeared_once(self,array:list) -> int:
        first=second=third=None
        found_first = found_second = found_third=False

        for i in array[:-1]:
            if not first:
                first=i
                continue
            if not second and i!=first:
                second=i
                continue
            if not third and i!=first and i!=second:
                third=i
                continue

            if i==first:
                found_first=True
                continue
            if i==second:
                found_second=True
                continue
            if i==third:
                found_third=True
                continue

            if i not in (first,second,third):
                return i

        if not found_first:
            return first
        if not found_second:
            return second
        if not found_third:
            return third
        else:
            if array[-1] not in (first,second,third):
                return array[-1]
            else:
                return -1

array = [5,7,8,5,0,8,5,7,8,7]
print(Solution().appeared_once(array))
