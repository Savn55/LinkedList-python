
#create a Node class with data and next pointer
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
#create linkedlist class with head pointing to None to allow pointing to head of linkedlist later 
class linkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_begining(self, new_item):
        new_node = Node(new_item)
        
        if self.head == None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
        
    def insert_at_position(self, position, new_item):
        new_node = Node(new_item)
        
        if self.head == None:
            self.head = new_node
            return
        
        temp = self.head
        
        if position == 0:
            #self.insert_at_begining(new_item)
            #return
            
            new_node.next = self.head
            self.head = new_node
            return
        
        for i in range(position-2):
            temp = temp.next
        
        
            #return print("can't place " + str(new_item) + " at begining.")
            
        
        new_node.next = temp.next
        temp.next = new_node
        
    def insert_at_end(self, new_item):
        new_node = Node(new_item)
        
        if self.head == None:
            self.head = new_node
            return
        
        last = self.head
        while (last.next):
            last = last.next
            
        last.next = new_node
        
    def del_at_position(self, position):
        if self.head == None:
            return print("Nothing to delete")
        
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp = None
            return
        
        for i in range(position-1):
            temp = temp.next
            
        if temp == None:
            return
        if temp.next == None:
            return
        
        next = temp.next.next
        temp.next = None
        temp.next = next
        
    def search(self, key):
        temp = self.head
        
        pos = 1
        while temp is not None:
            if temp.data == key:
                return print("found at position " + str(pos))
                #return print("search found.")
                
            temp = temp.next
            pos += 1
        return False
        
    def sortlist(self, head): #head here is to access the head of the list 
                              #from function call with llist.head
        current = head      
        index = Node(None)  #index obj of Node class
        
        if head == None:
            return
        else:
            while current is not None:
                index = current.next
                
                while index is not None:
                    if current.data > index.data:  #sorting ascending order
                        current.data, index.data = index.data, current.data #swapping values
                        
                    index = index.next
                current = current.next    
        
    def display(self):
        temp = self.head 
        while temp is not None:
            print(temp.data, end = " ")
            temp = temp.next

llist = linkedList()
llist.insert_at_begining(4)
llist.insert_at_begining(5)
llist.insert_at_begining(3)
llist.insert_at_begining(1)
llist.insert_at_position(3,2)
llist.display()
print('\n')
llist.insert_at_end(6)
llist.display()
print('\n')
llist.del_at_position(5)
llist.display()
print('\n')
llist.search(4)
print('\n')
llist.sortlist(llist.head)
llist.display()

#llist.insert_at_begining(0)
#llist.display()
        
