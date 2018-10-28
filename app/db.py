import flask
import psycopg2
import psycopg2.extras

def get_connection():
    if not hasattr(flask.g, 'dbconn'):
        flask.g.dbconn = psycopg2.connect(user = 'Kyzyl-ool', database = 'postgres')
        return flask.g.dbconn

def get_cursor():
    return get_connection().cursor(cursor_factory=psycopg2.extras.DictCursor)

def query_one(sql, **params):
    with get_cursor() as cur:
        cur.execute(sql, params)
        return dict(cur.fetchone())

def query_all(sql, **params):
    with get_cursor() as cur:
        cur.execute(sql, params)
        result = cur.fetchall()
        return {i:  dict(result[i]) for i in range(len(result))}
