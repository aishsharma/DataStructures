"""
Author: Aishwarya Sharma
"""
import logging
from typing import Any


class Underflow(Exception):
	def __str__(self):
		return "Stack is empty"


class Overflow(Exception):
	def __str__(self):
		return "Stack is full"


class ArrayStack:
	top = -1
	nodes = []
	size = 50

	def __init__(self, size: int = None):
		if size:
			self.size = size

	def push(self, item: Any) -> bool:
		if self.top == self.size - 1:
			raise Overflow()
		self.nodes.append(item)
		self.top += 1

	def pop(self) -> Any:
		if self.top == -1:
			raise Underflow()
		else:
			item = self.nodes.pop()
			self.top -= 1
			return item


if __name__ == '__main__':
	stack = ArrayStack(10)
	try:
		for i in range(11):
			stack.push(i + 1)
	except Overflow as err:
		logging.error(err)
	finally:
		print(stack.nodes)

	try:
		for i in range(11):
			print("Popped: {}".format(stack.pop()))
	except Underflow as err:
		logging.error(err)
	finally:
		print(stack.nodes)
