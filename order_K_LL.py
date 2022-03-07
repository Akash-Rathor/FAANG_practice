'''
Given K sorted linked lists of different sizes.
The task is to merge them in such a way that after merging they will be a single sorted linked list.
Solution with : 
Time Complexity: O(nk Logk)
Auxiliary Space: O(nk)

all test cases passed - GFG - 
'''

class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None


class Solution:
    #Function to merge K sorted linked list.
    def mergeKLists(self,arr,K):
        '''
        Input : head of K sorted Linked lists
        returns :  head of merged Linked list
        '''
        sortedLinks = []
        for i in arr:
            current = i
            while current:
                sortedLinks.append(current.data)
                current = current.next
        sortedLinks = sorted(sortedLinks)
        head = Node(sortedLinks[0])
        current = head
        for i in sortedLinks[1:]:
            current.next = Node(i)
            current = current.next

        
        current = head
        while current:
            print(current.data,end = ' -> ')
            current = current.next

A = Node(1)
b = A.next = Node(2)
c = b.next = Node(3)
B = Node(4)
d = B.next = Node(5)
d.next = Node(6)

C = Node(7)
C.next = Node(8)

arr = [C,A,B]

Solution().mergeKLists(arr,len(arr))