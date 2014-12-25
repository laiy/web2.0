import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os.path

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

from models import IndexHandler, SignupHandler, SigninHandler, AskHandler

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        (r'/', IndexHandler),
        (r'/signup', SignupHandler),
        (r'/login', SigninHandler),
        (r'/ask', AskHandler)
    ], template_path=os.path.join(os.path.dirname(__file__), "template"),
        static_path=os.path.join(os.path.dirname(__file__), "static"), debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
