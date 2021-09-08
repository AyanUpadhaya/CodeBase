#in linked list every element is connected to each other through a link

class Node:
    #node class
    def __init__(self,value):
        self.prev=None
        self.value=value
        self.next=None

class DoubleLinkedList:
    #DoubleLinkedList class
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def add(self,val):
        node=Node(val)
        if self.tail is None:
            self.tail=node
            self.head=node
            self.size+=1
        else:
            self.tail.next=node
	    #first to update tail then head will be the first node
            node.prev=self.head
            self.tail=node
            self.size+=1
    def __str__(self):
        vals=[] #empty list
        node=self.head #this node variable is local but assigned to self.head
        while node is not None:
             vals.append(node.value)
             node = node.next
        return f"[{','.join(str(val) for val in vals)}]" #list comprehension

mylist=DoubleLinkedList()
mylist.add(1)
mylist.add(2)
mylist.add(5)
mylist.add(7)
print(mylist)
