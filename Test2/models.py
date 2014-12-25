#!/usr/bin/env python
# coding=utf-8

#	> File Name: models.py
#	> Author: LY
#	> Mail: ly.franky@gmail.com
#	> Created Time: Wednesday, December 03, 2014 AM08:59:20 CST

import os.path
import tornado.web
import re
import sys

reload(sys) 
sys.setdefaultencoding('utf-8')

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        logout = self.get_argument('logout', None)
        f = open(os.path.join(os.path.dirname('__file__'), 'static', 'qusetionData', 'questions.txt'), 'r')
        questions = []
        for msg in f:
            question = Question(re.split(';', msg))
            questions.append(question)
        f.close()
        if logout:
            self.clear_cookie('name')
            self.redirect('/')
        elif self.get_cookie('name'):
            self.render('index.html', name=self.get_cookie('name'), questions=questions)
        else:
            self.render('index.html', name='', questions=questions)

class SignupHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('signinup.html', title='注册-SegmentFault', header='注册新帐号', button='注册')
    def post(self):
        name = self.get_argument('name', None)
        password = self.get_argument('password', None)
        if name and password:
            f = open(os.path.join(os.path.dirname('__file__'), 'static', 'userdata', 'users.txt'), 'a')
            f.write(','.join([name, password]) + '\n')
            f.close()
            self.set_cookie('name', name)
            self.redirect('/')

class SigninHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('signinup.html', title='登录-SegmentFault', header='登录到SegmentFault', button='登录')
    def post(self):
        name = self.get_argument('name', None)
        password = self.get_argument('password', None)
        if name and password:
            f = open(os.path.join(os.path.dirname('__file__'), 'static', 'userdata', 'users.txt'), 'r')
            for msg in f:
                (dataName, dataPassword) = re.split(',', msg)
                dataPassword = dataPassword[0:-1]
                if dataName == name and dataPassword == password:
                    self.set_cookie('name', name)
            f.close()
            self.redirect('/')

class AskHandler(tornado.web.RequestHandler):
    def get(self):
        if self.get_cookie('name'):
            self.render('ask.html', title='提出问题-SegmentFault', name=self.get_cookie('name'))
        else:
            self.render('ask.html', title='提出问题-SegmentFault', name='')
    def post(self):
        if self.get_cookie('name'):
            title = self.get_argument('title', None)
            tags = self.get_argument('tags', None)
            content = self.get_argument('content', None)
            if title and tags and content:
                f = open(os.path.join(os.path.dirname('__file__'), 'static', 'qusetionData', 'questions.txt'), 'a')
                f.write(';'.join(['0', '0', "回答", '0', self.get_cookie('name'), "刚刚", title, tags]) + '\n')
                f.close()
        self.redirect('/')

class Question(object):
    def __init__(self, infos):
        self.votes = infos[0]
        self.answers = infos[1]
        self.status = infos[2]
        self.views = infos[3]
        self.createdBy = infos[4]
        self.createdAt = infos[5]
        self.title = infos[6]
        self.category = infos[7]
        
