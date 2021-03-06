import tornado.ioloop
import tornado.web
import os
import sys
from tornado.options import define, options
from common.url_router import url_wrapper, include
from models import initDB
from sqlalchemy.orm import scoped_session, sessionmaker
from conf.base import BASEDB, engine

class App(tornado.web.Application):
    def __init__(self):
        initDB()
        handler = url_wrapper([
            (r"/users/", include("views.users.user_urls")),
            (r"/", include("view.homepage.homepage_urls"))
        ])
        settings = dict(
            debug=True,
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            template_path=os.path.join(os.path.dirname(__file__), "templates")

        )
        tornado.web.Application.__init__(self,handler, **settings)
        # scoped session is used to ensure thread safety
        self.db = scoped_session(
            sessionmaker(
                bind=engine, autocommit=False, autoflush=True,
                expire_on_commit=False
            )
        )

if __name__ == '__main__':
    print("Tornado server is on")
    options.parse_command_line()
    App().listen(8888, xheaders = True)
    tornado.ioloop.IOLoop.instance().start()

