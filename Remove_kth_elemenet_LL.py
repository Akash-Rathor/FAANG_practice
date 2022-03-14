'''
Given a Linked List and an integer k, remove the element at the kth position of the linked list.
Example
List: 1→3→4→7
k: 2
Result: 1→4→7
'''
class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


    def pp(self,node):
        curr = node
        while curr:
            print(curr.data,end=' -> ')
            curr = curr.next


class Solution:
	def removekthElement(self, head: ListNode, k: int) -> ListNode:
		if k>1:
			count = 1
			curr = head
			while count<k:
				pre = curr
				curr = curr.next
				nextnext = curr.next
				count+=1

			pre.next = nextnext
			del curr
			return head

		else:
			curr = head
			head = curr.next
			return head


A = ListNode(1)
A.next = ListNode(3)
A.next.next = ListNode(4)
A.next.next.next = ListNode(7)

# A.pp(A)

A.pp(Solution().removekthElement(A,1))