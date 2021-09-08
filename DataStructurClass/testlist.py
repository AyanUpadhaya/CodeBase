# First we need a node class, why?
# node will contain a value and it will know what is the next value
# but by default both can be none

# Now we will need a single linked list class,why?
# It will contain every node in order, how?
# it will have a head which is default None and will be updated
# it will be able show us all nodes
# it will be able to update the head


class Node:
	def __init__(self,data=None):
		self.data = data
		self.next = None

class Single_Linked_List:
	def __init__(self):
		self. head = None

	#method for showing all nodes
	def showNodes(self):
		mainval = self.head

		while mainval is not None:
			print(mainval.data)
			mainval = mainval.next

	def updateHead(self,new_data):
		new_node = Node(new_data)
		new_node.next = self.head #head will be second item
		self.head = new_node

list1 = Single_Linked_List()
list1.head = Node('4')

list2 = Node('5')
list3 = Node('6')
list4 = Node('7')

#connecting the nodes

list1.head.next = list2
list2.next = list3
list3.next = list4

list1.updateHead('3')

list1.showNodes()


# So how single link list is working?
# single link list has a head which is node itself
# we can create new node and assign it as the next node for head
# so every node will know what is the next node, which means we have to connect it
# head can be modified which means current head will be second node of the new node and
# new node will take place as the head


