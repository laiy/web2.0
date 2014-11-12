import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=2333, help="run on the given port", type=int)

class file:
    __slots__ = ('__name', '__size', '__filetype')
    def __init__(self, name, filetype, size):
        self.__name = name
        self.__filetype = filetype
        if size < 1024:
            self.__size = "%.2f b" % size
        elif size < 1024 * 1024:
            self.__size = "%.2f kb" % (float(size) / 1024)
        else:
            self.__size = "%.2f mb" % (float(size) / (1024 * 1024))
    def getFiletype(self):
        return self.__filetype
    def getName(self):
        return self.__name
    def getSize(self):
        return self.__size

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        playlist = self.get_argument('playlist', 'None')
        filepath = os.path.join(os.path.dirname(__file__), "static/songs")
        files = [];
        if playlist is not 'None':
            filenames = open(os.path.join(filepath, playlist)).read().splitlines()
        else:
            filenames = os.listdir(filepath)
        for filename in filenames:
            files.append(file(filename, os.path.splitext(filename)[1][1:], os.path.getsize(os.path.join(filepath, filename))))
        files.sort(key=lambda x:(x.getFiletype(), x.getName()))
        goBack = 'Flase' if playlist is 'None' else 'True'
        self.render('music.html', files=files, goBack=goBack)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r'/', IndexHandler)], template_path=os.path.join(os.path.dirname(__file__), "template"),
        static_path=os.path.join(os.path.dirname(__file__), "static"), debug=True)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

