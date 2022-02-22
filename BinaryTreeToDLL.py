class DllNode:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

class Node:

    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None

    inorder_transvered_list = []
    def inorder_transversal(self,node):
        '''
        LEFT - >
        ROOT - >
        RIGHT
        '''
        
        if node:
            self.inorder_transversal(node.left)
            root_node = node
            self.inorder_transvered_list.append(root_node.data)
            self.inorder_transversal(node.right)


        return self.inorder_transvered_list


    def BinaryTree_to_DLL(self,node=None):
        '''
        Function converts Binary Tree to Dubply Linked list

        : return : Doubly linked list head Node object
        '''
        if not node:
            return None
        else:
            inorder_transvered = self.inorder_transversal(node)
            head = DllNode(inorder_transvered[0])
            print(head.data,end=" <--> ")
            for i in inorder_transvered[1:]:
                new_node = DllNode(i)
                head.right = new_node
                new_node.left = head
                # print(new_node.data,end=" <--> ")

            return head




y = Node(3)
y.left = Node(4)
y.right = Node(5)
y.left.left = Node(6)
y.left.right = Node(7)
y.right.left = Node(8)
y.right.right = Node(9)
y.BinaryTree_to_DLL(y)



        