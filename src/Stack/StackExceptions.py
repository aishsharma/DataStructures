"""
Author: Aishwarya Sharma
"""


class Underflow(Exception):
	def __str__(self):
		return "Stack is empty"


class Overflow(Exception):
	def __str__(self):
		return "Stack is full"
