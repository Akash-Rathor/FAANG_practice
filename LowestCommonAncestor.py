class Node:

    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None


    def Lowest_common_ancestors(self,node,p,q):
        if not node:
            return None
        else:
            if node.left==p and node.right==q:
                return node
            else:
                left = self.Lowest_common_ancestors(node.left,p,q)
                right = self.Lowest_common_ancestors(node.right,p,q)

                if left and right:
                    return node
                return left or right

y = Node(3)
y.left = Node(4)
y.right = Node(5)
y.left.left = Node(6)
y.left.right = Node(7)
p = y.right.left = Node(8)
q = y.right.right = Node(9)

print(y.Lowest_common_ancestors(y,p,q).data)




        