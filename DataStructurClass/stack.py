#stack means arranging objects on over another.

"""stack data strcuture allows operations at one end wich can be called top of the stack.We can add elements or remove elements only form this en dof the stack.

In a stack the element insreted last in sequence will come out first as we can remove only from the top of the stack. 
Such feature is known as Last in First Out(LIFO) feature. 
The operations of adding and removing the elements is known as PUSH and POP. 
In the following program we implement it as add and and remove functions. 
We declare an empty list and use the append() and pop() methods to add and remove the data elements.
"""

class Stack:
	def __init__(self):
		self.stack = []

	def add(self, data):

		if data not in self.stack:
			self.stack.append(data)
			return True
		else:
			return False

	def peek(self):
		return self.stack[-1]

	def remove(self):
		if len(self.stack)<=0:
			print("No element in stack found")
		else:
			return self.stack.pop()

abstack =  Stack()

abstack.add('Mon')
abstack.add('Tue')
abstack.add('Wed')

abstack.remove() #for removing last item

print(abstack.peek())