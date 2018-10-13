'''This is Double-linked list module.'''

class Node():
	'''
	This is double-linked list's node.
	'''
	prev = 0
	next = 0

	def __init__(self, value):
		self.data = value

	def __str__(self):
		return self.data

	def get_prev(self):
		'''Returns previous node.'''
		return self.prev

	def get_next(self):
		'''Returns next node.'''
		return self.next

class DoubleLinkedList():
	'''
	Double-linked list.
	'''

	head = 0
	tail = 0

	def __insert_after_node(self, current, element):
		'''Inserts given node (element) before  'current' node.'''
		if current == 0 and self.head != 0:
			element.next = self.head
			self.head.prev = element
			self.head = element
			return
		if self.tail == 0:
			self.head = element
			self.tail = element
		else:
			if current.next != 0:
				element.next = current.next
				element.prev = current
				current.next.prev = element
				current.next = element
			else:
				element.next = 0
				element.prev = current
				current.next = element
				self.tail = element

	def __str__(self):
		'''Printing DoubleLinkedList.'''
		if self.head != 0:
			result = str(self.head.data)
		i = self.head.next
		while i != 0:
			result += ', ' + str(i.data)
			i = i.next

		return result

	def __remove_by_node(self, node):
		'''Removes given node.'''
		if node.next == 0 and node.prev == 0:
			del node
			self.head = 0
			self.tail = 0
		elif node.next == 0:
			node.prev.next = 0
			self.tail = node.prev
			del node
		elif node.prev == 0:
			node.next.prev = 0
			self.head = node.next
			del node
		else:
			node.prev.next = node.next
			node.next.prev = node.prev
			del node

	def __get_node(self, index):
		'''Returns node by index.'''
		i = self.head
		for _ in range(index):
			i = i.next
		return i

	def insert(self, index, value):
		'''Inserts value by index'''
		i = self.head
		for _ in range(index):
			i = i.next

		tmp_node = Node(value)
		self.__insert_after_node(i, tmp_node)

	def push(self, value):
		'''pushs new element to the end.'''
		tmp = Node(value)
		self.__insert_after_node(self.tail, tmp)

	def get(self, index):
		'''Returns data from node by index.'''
		return self.__get_node(index).data

	def pop(self):
		'''Removes node in the end and returns is.'''
		tmp = self.tail.data
		self.__remove_by_node(self.tail)
		return tmp

	def dump(self):
		'''Prints list's dump.'''
		print('head = {}'.format(self.head))
		print('tail = {}'.format(self.tail))
		print('data:')
		i = self.head
		while i != 0:
			print('[\n{}\nprev: {}\nnext:{}\ndata: {}\n]\n'.format(i, i.prev, i.next, i.data))
			i = i.next

	def unshift(self, value):
		'''pushs new element to the beggining of the list.'''
		tmp = Node(value)
		self.__insert_after_node(0, tmp)

	def shift(self):
		'''Removes element from the beginning.'''
		self.__remove_by_node(self.head)

	def len(self):
		'''Returns length of the list.'''
		i = self.head
		result = 0
		while i != 0:
			result += 1
			i = i.next

		return result

	def delete(self, elem):
		'''Removes element from the list.'''
		self.__remove_by_node(elem)

	def contains_element(self, elem):
		'''Checks if element is in list.'''
		i = self.head
		while i != elem:
			i.next
		return True if i == elem else False

	def contains(self, value):
		'''Checks if value is exist in list'''
		i = self.head
		while i != 0 and i.data != value:
			i = i.next
		return True if i != 0 and i.data == value else False

	def first(self):
		'''Returns first element.'''
		return self.head

	def last(self):
		'''Returns last element.'''
		return self.tail

	def delete_by_index(self, index):
		'''Deletes element by index and returns it.'''
		i = self.head
		for _ in range(index):
			i = i.next
		tmp = i.data
		self.__remove_by_node(i)
		return tmp

	def delete_by_value(self, value):
		'''Deletes by value'''
		i = self.head
		while (i != 0 and i.data != value):
			i = i.next

		if (i != 0):
			self.__remove_by_node(i)