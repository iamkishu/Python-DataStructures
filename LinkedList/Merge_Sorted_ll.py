

from multiprocessing import dummy


class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head=None
    
    def add_node(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)
    
    def print_list(self):
        ll = ''
        itr = self.head
        if itr is None:
            print("Linked List is empty");
        while itr:
            ll = ll + str(itr.data) + '-->' 
            itr = itr.next
        print(ll)
    
    def return_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr 


def merge_sorted_ll(l1, l2):
    if l1.head.next is None and l2.head.next is None:
        print ('Both lists are empty')
        return
    if l1.head.next is None:
        return l2
    if l2.head.next is None:
        return l1
    
    sorted_ll = LinkedList()
    itr1 = l1.head
    itr2 = l2.head

    while True:
        if itr1.data < itr2.data:
            sorted_ll.add_node(itr1.data)
            itr1 = itr1.next
        else:
            sorted_ll.add_node(itr2.data)
            itr2 = itr2.next

        if itr1 is None:
            lastnode = sorted_ll.return_last_node()
            lastnode.next = itr2
            break
        if itr2 is None: 
            lastnode = sorted_ll.return_last_node()
            lastnode.next = itr1
            break
    return sorted_ll
    


if __name__ == '__main__':
    l1 = [1, 3, 5, 7]
    l2 = [9, 10, 11]
    ll1 = LinkedList()
    for i in l1:
        ll1.add_node(i)
    ll1.print_list()
    ll2 = LinkedList()
    for i in l2:
        ll2.add_node(i)
    ll2.print_list()

    mll = merge_sorted_ll(ll1, ll2)
  
    # Display merged list
    print("Merged Linked List is:")
    mll.print_list()

        
