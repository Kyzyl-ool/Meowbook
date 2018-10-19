import unittest
from app import app
from flask import jsonify

class AppTest(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()

	def tearDown(self):
		pass

	def test_index(self):
		rv = self.app.get('/')
		self.assertEqual(200, rv.status_code)
		self.assertEqual(b'Hello, World!', rv.data)
		self.assertEqual('text/html', rv.mimetype)
		pass

	def test_form(self):
		rv = self.app.post('/form/', data = {'first_name': "Jesse", 'last_name': 'Ivanov'})
		self.assertEqual(b'{"first_name":"Jesse","last_name":"Ivanov"}\n', rv.data)

	def test_chats(self):
		rv = self.app.get('/chats/')
		self.assertEqual('application/json', rv.mimetype)
		self.assertEqual(200, rv.status_code)
		self.assertEqual(b'{"chats":["Meow","Gaw","Gavgav","Muu"],"mimetype":"application/json","status_code":"200 OK"}\n', rv.data)

	def test_contacts(self):
		rv = self.app.get('/contacts/')
		self.assertEqual('application/json', rv.mimetype)
		self.assertEqual(200, rv.status_code)
		self.assertEqual(b'{"contacts":["Cat","Dog","Mouse","Kitty","Cow","Bird"],"mimetype":"application/json","status_code":"200 OK"}\n', rv.data)

	def test_new_chat(self):
		rv = self.app.post('/new_chat/', data = {"chat_name": "HELLO"})
		self.assertEqual(200, rv.status_code)
		self.assertEqual('application/json', rv.mimetype)
		self.assertEqual(b'{"chat_name":"HELLO"}\n', rv.data)







if __name__ == "__main__":
	unittest.main()