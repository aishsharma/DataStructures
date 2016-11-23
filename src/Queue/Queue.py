"""
Author: Aishwarya Sharma
"""
from typing import Any


class Node:
	def __init__(self, value: Any = None, next: Any = None, previous: Any = None):
		self.value = value
		self.next = next
		self.previous = previous

	def __str__(self):
		return str(self.value)


class LinkedQueue:
	def __init__(self, front: Node = None, rear: Node = None):
		self.front = front
		self.rear = rear

	def enqueue(self, value: Any) -> None:
		temp = Node(value=value)
		if self.rear:
			temp.previous = self.rear
			self.rear.next = temp
			self.rear = temp
		else:
			self.front = self.rear = temp

	def dequeue(self) -> Node:
		if self.front:
			temp = self.front
			front = self.front = temp.next

			if front:
				front.previous = None
			temp.next = None
			return temp
		else:
			print("Queue is empty")
			return None

	def __str__(self):
		temp = self.front
		string = ""
		while temp:
			string += str(temp)
			if temp.next:
				string += ", "
			temp = temp.next
		if string == "":
			string = "Empty queue!"
		return string

	def get_reverse(self) -> str:
		temp = self.rear
		reverse = ""
		while temp:
			reverse += str(temp)
			if temp.previous:
				reverse += ", "
			temp = temp.previous
		return reverse


class ArrayQueue:
	size = 50
	queue = []
	front = -1
	rear = -1

	def __init__(self, size: int = None):
		if size:
			self.size = size

	def enqueue(self, value: Any) -> None:
		if self.rear == -1:
			self.front = self.rear = 0
			queue.append(value)
		elif self.rear == (self.size - 1) and self.front > 0:
			self.rear = 0
			self.queue[self.rear] = value
		elif self.rear < self.front - 1:
			self.rear += 1
			self.queue[self.rear] = value
		else:
			print("Queue is full!")

	def dequeue(self):
		if self.front > -1:
			if self.front < self.rear:
				self.front += 1
			elif self.front > self.rear:
				if self.front < self.size - 1:
					self.front += 1
				else:
					self.front = 0
			else:
				self.front = self.rear = -1
		else:
			print("Queue is empty!")

	def __str__(self):
		if self.front == -1:
			return ""
		i = self.front
		s = ""
		while i != self.rear:
			s += str(self.queue[i])
			if i == self.size - 1:
				i = 0
			else:
				i += 1

			if i != self.rear:
				s += ", "
		return s


if __name__ == '__main__':
	queue = LinkedQueue()
	for i in range(10):
		queue.enqueue(i)

	print(queue)
	# print(queue.get_reverse())
	#
	# if not queue.front.previous and not queue.rear.next:
	# 	print("Queue seems to be ok.")

	for i in range(10):
		queue.dequeue()
		print(queue)
	print(queue)
