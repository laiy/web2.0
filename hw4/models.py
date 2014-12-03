#!/usr/bin/env python
# coding=utf-8

#	> File Name: models.py
#	> Author: LY
#	> Mail: ly.franky@gmail.com
#	> Created Time: Tuesday, November 25, 2014 PM07:43:09 CST

import os.path
import tornado.web
import re

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
    def post(self):
        name = self.get_argument('name', None)
        gender= self.get_argument('gender', None)
        age = self.get_argument('age', None)
        type = self.get_argument('type', None)
        favoriteOS = self.get_argument('favoriteOS', None)
        Male = self.get_argument('Male', None)
        Female = self.get_argument('Female', None)
        age_from = self.get_argument('age_from', None)
        age_to = self.get_argument('age_to', None)
        seeking = 'MF' if Male and Female else 'M' if Male else 'F'
        errorLog = ''
        if not name:
            errorLog += 'Name is empty.'
        if age < '0' or age > '99' or not age.isdigit():
            errorLog += 'Bad age.'
        if gender  != 'M' and gender != 'F':
            errorLog += 'Bad gender.'
        if not re.match(r'[IE]{1}[NS]{1}[FT]{1}[JP]{1}', type):
            errorLog += 'Bad type.'
        if favoriteOS != 'Windows' and favoriteOS != 'Mac OS X' and favoriteOS != 'Linux' and favoriteOS != 'other':
            errorLog += 'Bad OS.'
        if seeking is not 'MF' and seeking is not 'M' and seeking is not 'F':
            errorLog += 'Bad seeking.'
        if age_from > age_to or age_from < '0' or age_from > '99' or not age_from.isdigit() or age_to < '0' or age_to > '99' or not age_to.isdigit():
            errorLog += 'Bad age from and to.'
        if errorLog is not '':
            self.render('results.html', errorLog=errorLog, matchs='')
            return
        personsData = open(os.path.join(os.path.dirname(__file__), 'assets', 'singles.txt'), 'r')
        matchs = []
        for personalMsg in personsData:
            msg = PersonMsg(re.split(',', personalMsg))
            degree = 0;
            if msg._seeking.find(gender) >= 0 and seeking.find(msg._gender) >= 0:
                if age_from <= msg._age <= age_to and msg._age_from <= age <= msg._age_to:
                    degree += 1;
                if msg._favoriteOS == favoriteOS:
                    degree += 2;
                for i in range(0, 4):
                    if msg._type[i] == type[i]:
                        degree += 1;
                if degree >= 3:
                    msg._rating = degree
                    matchs.append(msg)
        personsData.close()
        f = open(os.path.join(os.path.dirname(__file__), 'assets', 'singles.txt'), 'a')
        f.write(','.join([name, gender, age, type, favoriteOS, seeking, age_from, age_to]) + '\n')
        f.close()
        self.render('results.html', matchs=matchs, replace=replace, errorLog='')

def replace(name):
    filePath = os.path.join(os.path.dirname(__file__), 'assets', 'images')
    filenames = os.listdir(filePath)
    newName = name.replace(' ', '_').lower()
    if newName + '.jpg' in filenames:
        return newName
    else:
        return 'default_user'


class PersonMsg(object):
    def __init__(self, infos):
        self._name = infos[0];
        self._gender = infos[1];
        self._age = infos[2];
        self._type = infos[3];
        self._favoriteOS = infos[4];
        self._seeking = infos[5];
        self._age_from = infos[6];
        self._age_to = infos[7];
        self._rating = 0

