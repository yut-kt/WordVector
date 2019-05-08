# -*- coding: utf-8 -*-

from os import environ
from os.path import join, dirname
from dotenv import load_dotenv
from multiprocessing import cpu_count

load_dotenv(join(dirname(__file__), '.env'))
load_dotenv(join(dirname(__file__), '.env.default'))

DIMENSION = int(environ.get('DIMENSION'))
WINDOW = int(environ.get('WINDOW'))
MIN_COUNT = int(environ.get('MIN_COUNT'))
WORKERS = cpu_count() if int(environ.get('WORKERS')) == -1 else environ.get('WORKERS')
EPOCH = int(environ.get('EPOCH'))
SG = int(environ.get('SG'))
