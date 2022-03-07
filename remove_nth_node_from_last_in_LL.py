class Node:

    def  __init__(self,data):
        self.data = data
        self.next = None
        
class Solution:

    def removeNthFromEnd(self, head, n: int):
        '''
        Input : takes head of singly Linked List

        Returns : Head of same linked list with nth node removed from the end.

        Time complexity : O(N)
        Space complexity : O(N)
        '''
        nodes = []
        current = head
        while current:
            x = current
            nodes.append(current)
            current = current.next
            x.next = None

        nodes.pop(-n)
        if len(nodes)>=1:
            head = nodes[0]
            current = head
            if len(nodes)>1:
                for i in nodes[1:]:
                    current.next = i
                    current = current.next
                return head
            else:
                head.next = None
                return head
        else:
            return None


    def pprint(head):
        '''
        Pretty print the singly Linked list
        '''
        while head:
            print(head.data,end=' -> ')
            head = head.next


if __name__ == '__main__':
    A = Node(1)
    B = Node(2)
    C = Node(3)
    D = Node(4)
    E = Node(5)
    F = Node(6)
    A.next=B
    B.next=C
    C.next=D
    D.next=E
    E.next=F
    Solution().pprint(A)
    Solution().removeNthFromEnd(A,1)
    print('\n')
    Solution().pprint(A)