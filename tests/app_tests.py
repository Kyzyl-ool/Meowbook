import unittest
from app import app
from flask_jsonrpc.proxy import ServiceProxy
import psycopg2

class JSONRPCTest(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()
		self.server = ServiceProxy('http://127.0.0.1:5000/')

	def executeSQL(self, file, connection):
		file = open(file, 'r')
		sql = " ".join(file.readlines())
		cur = connection.cursor()
		cur.execute(sql)
		connection.commit()
		file.close()

	def setNewDBData(self):
		conn = psycopg2.connect(user = 'kyzyl-ool', database = 'template1')
		self.executeSQL('sql/MeowBook_DB_postgres_create-2.sql', conn)

	def test_get_users(self):
		self.setNewDBData()
		
		s = self.server.get_users('TestUser')
		# expected = {'id': '2fe4c96c-f4d6-4430-b23d-3ddbc67da184', 'jsonrpc': '2.0', 'result': {'0': {'name': 'root', 'nick': 'Koren', 'user_id': 0}}}


		self.assertEqual(s['result']['0']['nick'], 'TestNickname')
		# self.assertEqual(s['result']['1']['nick'], 'NeKoren')
		# print('--->', s, '<---', sep = '')

	def test_new_chat(self):
		self.setNewDBData()

		self.server.new_chat('NEWCHAT', True)

		tmp = self.server.get_chats(0)
		self.assertEqual(tmp['result']['1']['topic'], 'NEWCHAT')


	def test_new_message(self):
		self.setNewDBData()


		s = self.server.new_message(0, 0, 'Hello')
		# print(s)

		tmp = self.server.get_messages(0, 0)
		self.assertEqual(tmp['result']['0']['content'], 'Hello')



if __name__ == "__main__":
	unittest.main()