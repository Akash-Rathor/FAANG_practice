class Node:
    '''
    Node class to create a new node

    Node.key = key
    
    Node.next = None or address of a new node

    '''
    def __init__(self,key):
        self.key=key
        self.next = None


    
class LinkedList:

    def __init__(self):
        self.head = None
        
    
    def insert(self,key):
        '''
        Input a key to create a new node in the end of the linkedlist
        '''
        if not self.head:
            self.head = Node(key)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(key)

        
    def printll(self):
        '''
        Prints singly linkedlist
        '''
        if self.head==None:
            return None
        else:
            current = self.head
            while current:
                print(current.key,end=" --> ")
                current = current.next


    def deleteNode(self,Nodekey):
        '''
        Input a key of a node to be deleted

        :return:
        A linkedlist with a deleted node
        '''
        if self.head ==None:
            return "No Head found"
        else:
            current = self.head
            while current.next.key!=Nodekey:
                current = current.next
            temp = current.next
            current.next = temp.next
            del temp
            

            

ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.deleteNode(3)
ll.printll()