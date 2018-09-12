import tornado.web

from common.commons import http_response
from conf.base import ERROR_CODE


class HomepageHandle(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        http_response(self, ERROR_CODE['0'], 0)