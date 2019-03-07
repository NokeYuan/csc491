"""
Flask
"""
from flask import Flask
from flask import render_template
import json

from Main import get_block

app = Flask(__name__)


@app.route('/')
# TODO: Fill w/ main page


@app.route('/display')
def render_display():
    """
    Renders the display page with given blockchain
    :return:
    :rtype:
    """
    blockchain = get_block()
    json_chain = []
    json_chain.append(json.loads(blockchain[1]))
    return render_template('display.html', title='Display', block=json.loads(blockchain[1]))


if __name__ == '__main__':
    app.run()
