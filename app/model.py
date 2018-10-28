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

def add_new_chat(chat_id, is_group_chat, topic, last_message):
	execute("""
		INSERT INTO "Chat" VALUES (%(chat_id)s, %(is_group_chat)s, %(topic)s, %(last_message)s);
	""",
	chat_id = int(chat_id),
	is_group_chat = 't' if is_group_chat else 'f',
	topic=str(topic),
	last_message = int(last_message))
	commit()
	rollback()