"""
Author: Aishwarya Sharma
"""

import logging
from typing import Any

from src.Stack.StackExceptions import Underflow


class Node:
	data = None
	next = None

	def __init__(self, data: Any = None):
		self.data = data

	def __str__(self):
		return str(self.data)


class LinkedStack:
	top = None

	def push(self, item: Node) -> None:
		item.next = self.top
		self.top = item

	def pop(self):
		if self.top:
			temp = self.top
			self.top = self.top.next
			temp.next = None
			return temp
		else:
			raise Underflow

	def __str__(self):
		items = ""

		temp = self.top
		while temp:
			items += str(temp)
			if temp.next:
				items += ", "
			temp = temp.next
		return items


if __name__ == '__main__':
	stack = LinkedStack()
	try:
		for i in range(11):
			stack.push(Node(i + 1))
	finally:
		print(stack)

	try:
		for i in range(12):
			print("Popped: {}".format(stack.pop()))
	except Underflow as err:
		logging.error(err)
	finally:
		print(stack)
