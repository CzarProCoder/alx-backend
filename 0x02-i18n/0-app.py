#!/usr/bin/env python3
'''
Entry point to the flask app
'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    '''
    Render the index file from templates folder
    '''
    return render_template('0-index.html')
