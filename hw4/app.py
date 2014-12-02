#!/usr/bin/env python
# coding=utf-8

#	> File Name: app.py
#	> Author: LY
#	> Mail: ly.franky@gmail.com
#	> Created Time: Tuesday, November 25, 2014 PM07:41:31 CST

import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from models import IndexHandler
from tornado.options import define, options

define("port", default=2333, help="run on the given port", type=int)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r'/', IndexHandler)], template_path=os.path.join(os.path.dirname(__file__), "tpl"),
        static_path=os.path.join(os.path.dirname(__file__), "assets"), debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
