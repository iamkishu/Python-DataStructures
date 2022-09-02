class Treenode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        prefix = ' ' * self.get_level() * 3
        print(prefix +self.data)
        if len(self.children)>0:
            for child in self.children:
                child.print_tree()

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

def build_product_tree():
    root  = Treenode("Electronics")
    
    laptop = Treenode("Laptop")
    laptop.add_child(Treenode("Mac"))
    laptop.add_child(Treenode("Windows"))

    cellphone = Treenode("Cellphone")
    cellphone.add_child(Treenode("Android"))
    cellphone.add_child(Treenode("IOS"))

    tv = Treenode("TV")
    tv.add_child(Treenode("Samsung"))
    tv.add_child(Treenode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    return root


if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
    pass