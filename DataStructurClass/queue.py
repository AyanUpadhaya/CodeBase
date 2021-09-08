# Queue data structure - First in first out (Fifo)

"""
The queue data structure also means the same where the data elements are arranged in a queue. 
The uniqueness of queue lies in the way items are added and removed. 
The items are allowed at end but removed form the other end. So it is a First-in-First out method.

We can add elements by using insert() and remove elements by using pop method

""" 

class Queue:
	def __init__(self):
		self.queue = list()

	def add(self,data):
		if data not in self.queue:
			self.queue.insert(0,data)
			return True
		return False

	def showelements(self):
		for elm in self.queue:
			print(elm)

	def remove(self):
		if len(self.queue)>0:
			return self.queue.pop()
		return "No element found"

theQueue = Queue()

theQueue.add('mon')
theQueue.add('tue')
theQueue.add('wed')

theQueue.remove()
theQueue.showelements()