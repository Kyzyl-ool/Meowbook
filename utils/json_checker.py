import json

def json_equal(str1, str2):
	return to_json(str1) == to_json(str2)


def to_json(string):
	return json.loads(string)


if __name__ == '__main__':
	assert json_equal('{"code": 200, "list": [1, 2, 3]}', '{"list": [3, 2, 1], "code": 200}')