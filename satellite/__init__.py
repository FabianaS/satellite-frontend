from flask import Flask

__version__ = '1.0'
__name__ = 'satellite_ce'

app = Flask(__name__)
app.config.from_object('config')

