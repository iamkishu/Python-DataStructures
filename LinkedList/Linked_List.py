class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linked_List:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head == None:
            print("Linked List is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next 
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)
        
    def get_length(self):
        if self.head is None:
            return 0
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            print('Not a valid index')
            return
        
        if index==0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break 
            itr = itr.next
            count += 1

    def insert_at(self, data, index):
        if index < 0 or index >= self.get_length():
            print('Not a valid index')
            return
        
        if index==0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
    
    def remove_by_value(self, value):
        itr = self.head
        if itr.data == value:
            self.head = itr.next
            return

        while itr:
            if value == itr.next.data:
                itr.next = itr.next.next
                return
            itr = itr.next

    def insert_after_value(self, value, data):
        itr = self.head
        node = Node(data, None)        
        while itr:
            if itr.data == value:
                node.next = itr.next
                itr.next = node
                break
            itr = itr.next
    
    def reverse_list(self):
        temp = None
        itr = self.head
        while itr:
            temp_next = itr.next
            itr.next = temp
            temp = itr
            itr = temp_next
        self.head = temp
    
    def insert_at_sorted_point(self, data, ll):
        itr = ll.head
        if itr is None:
            ll.head = Node(data, None )
            return
        
        while itr:
            if itr.data > data:
                ll.head = Node(data, itr)
                break
            elif itr.data < data :
                itr.next = Node(data, itr.next)
                break
            itr = itr.next
        

    def sort_K_lists(self, lists):
        sorted_list = Linked_List()
        for list in lists:
            for val in list:
                sorted_list.insert_at_sorted_point(val, sorted_list)
        sorted_list.print()
        


    
if __name__ == '__main__':
    ll = Linked_List()
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(1)
    ll.insert_at_end(4)
    ll.insert_at_end(5)
    ll.print()
    print(ll.get_length())
    ll.remove_at(2)
    ll.print()
    ll.insert_at(3, 2)
    ll.print()
    ll.remove_by_value(3)
    ll.print()
    ll.insert_after_value(2,3)
    ll.insert_after_value(3,4)
    ll.insert_after_value(5,6)
    ll.print()
    ll.reverse_list()
    ll.print()
    ll.sort_K_lists([[3,2,1,0],[6,4,5]])