from .db import *

def get_user():
    return query_one("""
    SELECT * FROM "User";
    """)
