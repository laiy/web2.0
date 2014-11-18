#!/usr/bin/env python
# coding=utf-8

#	> File Name: models.py
#	> Author: LY
#	> Mail: ly.franky@gmail.com
#	> Created Time: Monday, November 17, 2014 PM07:59:52 CST

import os.path
import glob
import tornado.web

class MovieInfo(object):
    def __init__(self, filePath):
        movieFile = open(os.path.join(filePath, 'info.txt'))
        (self.title, self.year, self.rating, self.total) = movieFile.read().splitlines()
        self.dir = filePath.split(os.sep)[-1]

class ReviewMsg(object):
    def __init__(self, quote, rating, reviewer, company):
        self.quote = quote
        self.rating = rating
        self.reviewer = reviewer
        self.company = company

class Reviews(object):
    def __init__(self, filePath):
        self.left = []
        self.right = []
        reviews = glob.glob(os.path.join(filePath, 'review[0-9]*.txt'))
        self._len = len(reviews)
        reviews.sort()
        for i in range(self._len):
            file = open(reviews[i])
            (quote, rating, reviewer, company) = file.read().splitlines()
            msg = ReviewMsg(quote, rating, reviewer, company)
            self.left.append(msg) if i < self._len / 2 else self.right.append(msg)

class ReviewsModule(tornado.web.UIModule):
    def render(self, reviews):
        return self.render_string('includes/review.html', reviews=reviews)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        film = self.get_argument('film', 'tmnt')
        filePath = os.path.join(os.path.dirname(__file__), 'assets', 'movies', film)
        movieInfo = MovieInfo(filePath)
        overviewsData = open(os.path.join(filePath, 'generaloverview.txt'))
        overviews = []
        for overview in overviewsData:
            (head, sep, inside) = overview.partition(':')
            overviews.append((head, inside))
        reviews = Reviews(filePath)
        self.render('movie.html', movieInfo=movieInfo, overviews=overviews, reviews=reviews)

