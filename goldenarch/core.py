# -*- coding: utf-8 -*-

"""
goldenarch.py
~~~~~~~~~~~~~

Serves crap. Fast.
"""

import os
import sys

import static

PORT = os.environ.get('PORT', 8000)
STATIC_DIR = sys.argv[1]


app = static.Cling(STATIC_DIR)


def cli():
    print 'Serving crap. Fast.'

    cmd = (
        'gunicorn goldenarch:app '
        '-b "0.0.0.0:{port}" '
        '-w 16 -k gevent -t 2 '
        '--name goldenarch'
    ).format(port=PORT)

    os.system(cmd)


if __name__ == '__main__':
    try:
        cli()
    except KeyboardInterrupt:
        sys.exit()