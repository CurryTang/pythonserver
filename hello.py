import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    """
        Main handler
    """
    def get(self, *args, **kwargs):
        self.write("Hello World!")


application = tornado.web.Application([
    (r"/", MainHandler)
])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    