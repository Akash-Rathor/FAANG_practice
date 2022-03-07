class Node:
    def __init__(self,x):
        self.data = x
        self.next = None

class Solution:
    #Function to merge K sorted linked list.
    def mergeKLists(self,arr,K):
        # print([i.data for i in arr])
        sortedLinks = sorted(arr,key = lambda x : x.data)
        i = 0
        while i<len(sortedLinks):
            current = sortedLinks[i]
            while current.next:
                current = current.next
            i+=1
            if i<len(sortedLinks):
                current.next = sortedLinks[i]
                current = current.next
            
        head = sortedLinks[0]
        while head:
            print(head.data,end=' -> ')
            head = head.next
            
        # return sortedLinks[0]


A = Node(1)
b = A.next = Node(2)
c = b.next = Node(3)
B = Node(4)
d = B.next = Node(5)
d.next = Node(6)

C = Node(7)
C.next = Node(8)

arr = [C,A,B]
print(Solution().mergeKLists(arr,len(arr)))