#!/usr/bin/env python3
'''
Entry point to the flask app
'''
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config():
    '''
    Contain the languages
    '''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    '''
    Render the index file from templates folder
    '''
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
