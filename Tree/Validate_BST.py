import collections
class BST:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right
    
    def level_order_traversal(self):
        traversal_q = collections.deque()
        traversal_q.append(self)
        output = []
        while len(traversal_q):
            curr = traversal_q.popleft()
            output.append(curr.data)
            if curr.left is not None:
                traversal_q.append(curr.left)
            if curr.right is not None:
                traversal_q.append(curr.right)
        print(output)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    

if __name__=='__main__':
    tree = BST(100)
    tree.left = BST(50)
    tree.right = BST(200)
    tree.left.left = BST(25)
    tree.left.right = BST(75)
    tree.right.right = BST(1000)
    tree.level_order_traversal()
    arr = tree.in_order_traversal()
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            print("Not a valid tree")


