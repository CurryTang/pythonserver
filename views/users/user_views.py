import tornado.web
from tornado.escape import json_decode

from common.commons import http_response
from conf.base import ERROR_CODE

import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime
from models import Users

""" 
Configure logging functionality
"""

LOG_PATH = "log/users/users.log"
logger = logging.getLogger("Users")
logger.setLevel(logging.DEBUG)
handler = TimedRotatingFileHandler(
    LOG_PATH, when = "D",
    interval=1, backupCount=30
)
formatter = logging.Formatter(
    "%(asctime)s \%(filename)s[line:%(lineno)d] %(levelname)s %(message)s"
)
handler.suffix = "%Y%m%d"
handler.setFormatter(formatter)
logger.addHandler(handler)



class RegistHandle(tornado.web.RequestHandler):

    @property
    def db(self):
        return self.application.db

    def post(self):
        try:
            args = json_decode(self.request.body)
            phone = args['phone']
            verify_code = args['code']
        except:
            logger.info("RegistHandle: Requested Argument Invalid")
            http_response(self, ERROR_CODE['1001'], 1001)
            return
        # OK response

        ex_user = self.db.query(Users).filter_by(phone=phone).first()
        if ex_user:
            http_response(self, ERROR_CODE['1002'], 1002)
            self.db.close()
            return
        else:
            logger.debug('RegistHandle: Successfully insert db, user %s' % phone)
            create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            add_user = Users(phone, create_time)
            self.db.add(add_user)
            self.db.commit()
            self.db.close()
            logger.debug("RegistHandle: regist successfully")
            http_response(self, ERROR_CODE['0'], 0)

