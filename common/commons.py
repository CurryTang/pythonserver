import json


def http_response(self, msg, code):
    self.write(json.dumps(
        {"data": {
            "msg":msg,
            "code": code
        }}
    ))


