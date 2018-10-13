import unittest

import sys
from os import path
sys.path.append(path.dirname(path.dirname(__file__))+'/app')

from DoubleLinkedList import DoubleLinkedList

class TestDoubleLinkedList(unittest.TestCase):
	

	def test_init(self):	
		A = DoubleLinkedList()
		self.assertEqual(A.tail, 0)
		self.assertEqual(A.head, 0)

	def test_push_pop(self):
		A = DoubleLinkedList()
		A.push(1)
		self.assertEqual(A.get(0), 1)
		A.push('str')
		self.assertEqual(A.get(1), 'str')
		A.push([1, 2, 3])
		self.assertEqual(A.get(2), [1, 2, 3])
		A.push({1: 'word1', 2: 'word2', 3: 'JHAGSDJHASGD'})
		self.assertEqual(A.get(3), {1: 'word1', 2: 'word2', 3: 'JHAGSDJHASGD'})
		A.push((4, 6, 5, 10, 1, 1))
		self.assertEqual(A.get(4), (4, 6, 5, 10, 1, 1))

		self.assertEqual(A.delete_by_index(0), 1)
		self.assertEqual(A.delete_by_index(3), (4, 6, 5, 10, 1, 1))
		self.assertEqual(A.delete_by_index(1), [1, 2, 3])
		self.assertEqual(A.delete_by_index(0), 'str')
		self.assertEqual(A.delete_by_index(0), {1: 'word1', 2: 'word2', 3: 'JHAGSDJHASGD'})
		self.assertEqual(A.head, 0)
		self.assertEqual(A.tail, 0)

	def test_unshift_shift(self):
		A = DoubleLinkedList()
		A.unshift(4)
		self.assertEqual(A.get(0), 4)
		A.unshift(7)
		self.assertEqual(A.get(0), 7)
		A.unshift([1, 2, 3, 5])
		self.assertEqual(A.get(0), [1, 2, 3, 5])

		A.shift()
		self.assertEqual(A.get(1), 4)
		self.assertEqual(A.get(0), 7)
		A.shift()
		A.shift()
		self.assertEqual(A.head, 0)
		self.assertEqual(A.tail, 0)

	def test_len_delete(self):
		A = DoubleLinkedList()
		for i in range(100):
			A.unshift(i)

		self.assertEqual(A.len(), 100)
		A.shift()
		self.assertEqual(A.len(), 99)

		for i in range(99):
			self.assertEqual(A.get(0), 98-i)
			A.delete(A.head)

	def test_contains(self):
		A = DoubleLinkedList()
		for i in range(1, 100):
			A.push('*' * i)

		for i in range(1, 100):
			self.assertEqual(A.contains('*' * i), True)
		
		for i in range(1, 50):
			A.delete_by_index(i)

		for i in range(1, 50):
			self.assertEqual(A.contains('*' * (2*i)), False)

	def test_first_last(self):
		A = DoubleLinkedList()
		for i in range(100):
			A.push(str(i))

		for i in range(50):
			self.assertEqual(A.first().data, str(i))
			self.assertEqual(A.last().data, str(99-i))
			A.shift()
			A.pop()

	def test_connectivity(self):
		A = DoubleLinkedList()
		for n in range(100):
			A.push(n)
			i = A.head
			if n > 0:
				self.assertNotEqual(i.next, 0)
				i = i.next
				while i.next != 0:
					self.assertEqual(i.prev.next, i)
					self.assertEqual(i.next.prev, i)
					i = i.next
			else:
				self.assertEqual(i.prev, 0)
				self.assertEqual(i.next, 0)

	def test_delete_by_value(self):
		a = DoubleLinkedList()
		a.push(2)
		a.push(3)
		a.delete_by_value(2)
		self.assertEqual(a.get(0), 3)



if __name__ == '__main__':
	unittest.main()