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
        error = self.get_argument('error', None)
        if error == 'incomplete':
            self.render('sorry.html', errorMsg="You didn't fill the form completely.")
        elif error == 'badCard':
            self.render('sorry.html', errorMsg="You didn't provide a valid card number.")
        else:
            self.render('buyagrade.html')
    def post(self):
        name = self.get_argument('name', None)
        section = self.get_argument('section', None)
        creditCard = self.get_argument('creditCard', None)
        cardType = self.get_argument('cardType', None)
        if not name or not section or not creditCard or not cardType:
            self.redirect('/?error=incomplete')
        elif not isValid(creditCard, cardType):
            self.redirect('?error=badCard')
        else:
            f = open(os.path.join(os.path.dirname(__file__), 'assets', 'suckers.txt'), 'a')
            f.write(';'.join([name, section, creditCard, cardType]) + '\n')
            f.close()
            f = open(os.path.join(os.path.dirname(__file__), 'assets', 'suckers.txt'), 'r')
            fileContent = f.read();
            f.close();
            self.render('sucker.html', name=name, section=section, creditCard=creditCard, fileContent=fileContent)

def isValid(creditCard, cardType):
    cardNumber = creditCard.replace('-', '')
    if cardType == 'Visa':
        if re.compile('^4[0-9]{15}$').match(cardNumber) != None:
            return Luhn(cardNumber)
    else:
        if re.compile('^5[0-9]{15}$').match(cardNumber) != None:
            return Luhn(cardNumber)
    return False

def Luhn(number):
    numberList = [int(x) for x in str(number)]
    total = sum(x for i, x in enumerate(numberList) if i % 2 != 0) + sum(sum(divmod(2 * x, 10)) for i, x in enumerate(numberList) if i % 2 == 0)
    return total % 10 == 0

