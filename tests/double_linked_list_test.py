import unittest
from DoubleLinkedList import DoubleLinkedList

class TestDoubleLinkedList(unittest.TestCase):
	

	def test_init(self):	
		A = DoubleLinkedList()
		self.assertEqual(A.tail, 0)
		self.assertEqual(A.head, 0)

	def test_add_pop(self):
		A = DoubleLinkedList()
		A.add(1)
		self.assertEqual(A.get(0), 1)
		A.add('str')
		self.assertEqual(A.get(1), 'str')
		A.add([1, 2, 3])
		self.assertEqual(A.get(2), [1, 2, 3])
		A.add({1: 'word1', 2: 'word2', 3: 'JHAGSDJHASGD'})
		self.assertEqual(A.get(3), {1: 'word1', 2: 'word2', 3: 'JHAGSDJHASGD'})
		A.add((4, 6, 5, 10, 1, 1))
		self.assertEqual(A.get(4), (4, 6, 5, 10, 1, 1))

		self.assertEqual(A.pop(0), 1)
		self.assertEqual(A.pop(3), (4, 6, 5, 10, 1, 1))
		self.assertEqual(A.pop(1), [1, 2, 3])
		self.assertEqual(A.pop(0), 'str')
		self.assertEqual(A.pop(0), {1: 'word1', 2: 'word2', 3: 'JHAGSDJHASGD'})
		self.assertEqual(A.head, 0)
		self.assertEqual(A.tail, 0)

	def test_connectivity(self):
		A = DoubleLinkedList()
		for n in range(100):
			A.add(n)

			
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


if __name__ == '__main__':
	unittest.main()


