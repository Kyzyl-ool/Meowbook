from .db import *

def get_user():
    return query_one("""
    SELECT * FROM "User";
    """)

def get_users_list_by_mask(mask):
    return query_all("""
        SELECT * FROM "User"
        WHERE "name" LIKE %(mask)s;
    """, mask = str(mask))

def get_chats_list():
	return query_all("""
		SELECT * FROM "Chat";
	""")

def add_new_chat(is_group_chat, topic, last_message):
	execute("""
		INSERT INTO "Chat" (is_group_chat, topic, last_message) VALUES (%(is_group_chat)s, %(topic)s, %(last_message)s);
	""",
	is_group_chat = 't' if is_group_chat else 'f',
	topic=str(topic),
	last_message = int(last_message))
	commit()

def add_new_message(chat_id, user_id, content, sent):
	execute("""
		INSERT INTO "Message" (chat_id, user_id, content, sent) VALUES (%(chat_id)s, %(user_id)s, %(content)s, %(sent)s);
		""",
		chat_id = int(chat_id), user_id = int(user_id), content = str(content), sent = sent
	)
	commit()