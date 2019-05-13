import unittest
from app import app
from flask_jsonrpc.proxy import ServiceProxy
import psycopg2
import config

class JSONRPCTest(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()
		self.server = ServiceProxy('http://127.0.0.1:5000')
		conn = psycopg2.connect(user = config.TEST_DATABASE_USER, database = config.TEST_DATABASE_NAME)
		self.executeSQL(config.DATABASE_REFILL_SQL_FILE, conn)

	def executeSQL(self, file, connection):
		file = open(file, 'r')
		sql = " ".join(file.readlines())
		cur = connection.cursor()
		cur.execute(sql)
		connection.commit()
		file.close()

	# def test_get_users(self):
	# 	self.setNewDBData()
	# 	s = self.server.get_users('TestUser')

	# 	self.assertEqual(s['result']['0']['nick'], 'TestNickname')
	# 	# self.assertEqual(s['result']['1']['nick'], 'NeKoren')
	# 	# print('--->', s, '<---', sep = '')

	def test_new_chat(self):
		self.server.add_new_member_to_chat(0, self.server.new_chat('NEWCHAT', 't')['result']['0']['chat_id'])
		tmp = self.server.get_chats(0)
		print(tmp)
		# self.assertEqual(tmp['result']['1']['topic'], 'NEWCHAT')


	def test_new_message(self):
		s = self.server.new_message(0, 0, 'Hello')
		tmp = self.server.get_messages(0)
		self.assertEqual(tmp['result']['0']['content'], 'Hello')



if __name__ == "__main__":
	unittest.main()