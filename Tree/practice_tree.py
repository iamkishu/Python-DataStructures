from sys import prefix
from tkinter.tix import Tree


class Treenode:
    def __init__(self, name, desig):
        self.name = name
        self.desig = desig
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level+=1
            p = p.parent
        return level
    
    def print_tree(self, selc):
        prefix = ' ' * self.get_level() * 3
        if selc == 'name':
            print(prefix + self.name)
        elif selc == 'desig':
            print(prefix + self.desig)
        else:
            print(prefix + self.name + ' (' + self.desig + ')')

        for child in self.children:
            child.print_tree(selc)

if __name__ == '__main__':
    CEO_Node = Treenode('Nipul', 'CEO')
    CTO_Node = Treenode('Chinmay', 'CTO')
    IH_Node = Treenode('Vishwa', 'Infra Head')
    CM_Node = Treenode('Dhaval','Cld Mng')
    AM_Node = Treenode('Abi','App Mng')
    AH_Node = Treenode('Aamir', 'App Head')
    HR_Node = Treenode('Gels', 'HR')
    RM_Node = Treenode('Peter','Rcrtmnt Mng')
    PM_Node = Treenode('Waqas', 'Policy Manager')

    CEO_Node.add_child(CTO_Node)
    CEO_Node.add_child(HR_Node)

    CTO_Node.add_child(IH_Node)
    CTO_Node.add_child(AH_Node)

    HR_Node.add_child(RM_Node)
    HR_Node.add_child(PM_Node)

    IH_Node.add_child(CM_Node)
    IH_Node.add_child(AM_Node)

    CEO_Node.print_tree('desig')