import os
from flask import Flask
import logging


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def hello():
    return "Hello World!"
    print(os.environ['APP_SETTINGS'])
    print('whatever')
    logging.basicConfig(level = logging.INFO)
    logging.debug('whatever debug')
    logging.info('whatever info')
    logging.warning('whatever warning')
    logging.error('whatever error')
    logging.critical('whatever critical')


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()