from array import array
import collections

class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def pre_order_traversal(self):
        elements = []

        elements.append(self.data)
        
        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        
        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements
 
    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data
        
    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
            
        return self

    def invert_tree(self):
        tempright = self.right
        templeft = self.left
        self.left = tempright
        self.right = templeft
        if tempright is None:
            return
        else:
            tempright.invert_tree()
        if templeft is None:
            return
        else:
            templeft.invert_tree()
    
    def max_depth(self):
        if self is None:
            return 0
        if self.right is None and self.left is None:
            return 1
        if self.right is None:
            return 1 + self.left.max_depth()
        if self.left is None:
            return 1 + self.right.max_depth()
        return 1 + max(self.right.max_depth(), self.left.max_depth())

    def level_order_traversal(self):
        de = collections.deque([self])
        level_array=[self.data]
        print(self.data)
        while len(de) != 0:
            el = de.popleft()
            if el.left:
                level_array.append(el.left.data)
                de.append(el.left)
            if el.right:
                level_array.append(el.right.data)
                de.append(el.right)
        return level_array



def twin_tree(t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is not None and t2 is not None:
            return (twin_tree(t1.right, t2.right) and twin_tree(t1.left, t2.left))  
        return False

if __name__ == '__main__':
    elements = [5,3,7,4,6,1,9,2,8,]
    root = BinarySearchTree(elements[0])
    for i in elements:
        root.add_child(i)
    print(root.pre_order_traversal())
    root.invert_tree()
    print(root.pre_order_traversal())
    print(root.level_order_traversal())
    #print(root.in_order_traversal())
    #print(root.pre_order_traversal())
    #print(root.post_order_traversal())
    #print(root.search(4))
    #print(root.find_min())
    #print(root.find_max())
    #print(root.max_depth())
    #print(root.delete(5))
    #print(root.in_order_traversal())
    '''elements = [5,3,7,4,6,1,9,2,8]
    t1 = BinarySearchTree(elements[0])
    for i in elements:
        t1.add_child(i)
    elements = [5,3,7,4,6,1,9,2,8]
    t2 = BinarySearchTree(elements[0])
    for i in elements:
        t2.add_child(i)
    print(twin_tree(t1, t2))'''
