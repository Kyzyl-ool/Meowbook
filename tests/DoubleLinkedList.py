class Node(object):
	prev = 0
	next = 0
	data = 0


class DoubleLinkedList(object):
	'''
		Double-linked list.
		
		add(value) - adds new value to the end of the list
		insert(index, value) - adds new value to the list after node with given index


	'''

	head = 0
	tail = 0

	def __insert_after_node(self, current, element):
		'''Inserts given node (element) before  'current' node.'''
		if (current == 0):
			print('Error: null index!!!')
		if (current.next != 0):
			element.next = current.next
			element.prev = current
			current.next.prev = element
			current.next = element
		else:
			element.next = 0
			element.prev = current
			current.next = element
	def insert(self, index, value):
		'''Inserts value by index'''
		i = self.head
		for _ in range(index):
			i = i.next

		tmp_node = Node()
		tmp_node.data = value
		self.__insert_after_node(i, tmp_node)

	def add(self, value):
		'''Adds new value at the end of the list.'''
		if (self.tail == 0):
			self.head = Node()
			self.tail = self.head
			self.head.data = value
		else:
			self.tail.next = Node()
			self.tail.next.data = value
			self.tail.next.prev = self.tail
			self.tail = self.tail.next

	def __str__(self):
		'''Printing DoubleLinkedList.'''
		if (self.head != 0):
			result = str(self.head.data)
		i = self.head.next
		while i != 0:
			result += ', ' + str(i.data)
			i = i.next

		return result

	def __get_node(self, index):
		'''Returns node by index.'''
		i = self.head
		for _ in range(index):
			i = i.next
		return i

	def get(self, index):
		'''Returns data from node by index.'''
		return self.__get_node(index).data

	def __remove_by_node(self, node):
		'''Removes given node'''
		if (node.next == 0 and node.prev == 0):
			del node
			self.head = 0
			self.tail = 0
		elif (node.next == 0):
			node.prev.next = 0
			self.tail = node.prev
			del node
		elif (node.prev == 0):
			node.next.prev = 0
			self.head = node.next
			del node
		else:
			node.prev.next = node.next
			node.next.prev = node.prev
			del node

	def pop(self, index):
		'''Removes node by index and returned it.'''
		i = self.head
		for _ in range(index):
			i = i.next
		result = i.data
		self.__remove_by_node(i)
		return result

	def dump(self):
		'''Prints list's dump.'''
		print('head = {}'.format(self.head))
		print('tail = {}'.format(self.tail))
		print('data:')
		i = self.head
		while (i != 0):
			print('[\n{}\nprev: {}\nnext:{}\ndata: {}\n]\n'.format(i, i.prev, i.next, i.data))
			i = i.next
