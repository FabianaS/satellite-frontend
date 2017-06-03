# ----------------------------------------------------------------
# SATELLITE GENERAL CONFIGURATION
# ----------------------------------------------------------------
# This file contains all the configurations of the Satellite App.
# This file contains one configuration per line.
#
#
# Turns on debugging features in Flask
DEBUG = True
#
# For use in application emails
MAIL_FROM_EMAIL = "info@satellite-app.com"
#
# This is a secret key that is used by Flask to sign cookies.
# It’s also used by extensions like Flask-Bcrypt. You should
# define this in your instance folder to keep it out of version
# control.
SECRET_KEY = ''
#
# Configuration for the Flask-Bcrypt extension
BCRYPT_LEVEL = 12
#
# ----------------------------------------------------------------
# SERVER CONFIGURATION
# ----------------------------------------------------------------
PORT = 5001
#
# ----------------------------------------------------------------
# SATELLITE DATABASE CONFIGURATION
# ----------------------------------------------------------------
# See https://flask-pymongo.readthedocs.io/en/latest/ for more
# MongoDB configuration parameters
DATABASE = 'MongoDB'
MONGO_URI = ''
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_AUTO_START_REQUEST = True
MONGO_DBNAME = 'satellite'
MONGO_USERNAME = ''
MONGO_PASSWORD = ''
