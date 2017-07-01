"""
Author: Aishwarya Sharma
"""
from typing import Any


class Node:
	key = None
	value = None
	left_child = None
	right_child = None

	def __init__(self, key: Any, value: Any):
		self.key = key
		self.value = value


class BinarySearchTree:
	root = None

	def insert(self, root: Node, key: Any, value: Any) -> Node:
		if root:
			if key < root.key:
				root.left_child = self.insert(root=root.left_child, key=key, value=value)
			else:
				root.right_child = self.insert(root=root.right_child, key=key, value=value)
		else:
			root = Node(key=key, value=value)

		return root

	def search_recursive(self, key: Any, node: Node) -> Node:
		if not node or node.key == key:
			return node
		elif key < node.key:
			return self.search_recursive(key=key, node=node.left_child)
		else:
			return self.search_recursive(key=key, node=node.right_child)

	def search_iterative(self, key:Any, node: Node) -> Node:
		current_node = node
		while current_node:
			if key == current_node.key:
				return current_node
			elif key < current_node.key:
				current_node = current_node.left_child
			else:
				current_node = current_node.right_child
		return None

	def find_min(self): # Get smallest node in the tree
		current_node = self.root
		while current_node.left_child:
			current_node = current_node.left_child
		return current_node

