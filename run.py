#!/usr/bin/python
# run.py
import os
from satellite import app

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 7443))
    app.run('127.0.0.1', port)
