#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： fushaoshan
# datetime： 2021/5/18 11:32 上午
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to My Watchlist!'

#加了一行注释
