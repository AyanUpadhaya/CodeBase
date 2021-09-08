class Node:
	def __init__(self,dataval=None):
		self.dataval = dataval
		self.nextval = None

class SingleLinkedList:
	def __init__(self):
		self.headval =  None
	#print the linked list
	def listprint(self):
		printval = self.headval

		while printval is not None:
			print(printval.dataval)
			printval = printval.nextval

	def AtBegining(self,newdata):
		NewNode = Node(newdata)

		#update the new nodes next val to existing node

		NewNode.nextval = self.headval #head is going to be 2nd element of new node
		self.headval = NewNode #and current head will be replaced by new node



list1 = SingleLinkedList()

list1.headval = Node('Ayan')

l2 = Node('Rajib')
l3 = Node('Shajid')

#connect nodes

list1.headval.nextval = l2

l2.nextval = l3

list1.AtBegining('Rahul')


list1.listprint()
