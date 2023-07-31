import time
from ppadb.client import Client as AdbClient

def connect():
    client = AdbClient(host="217.0.0.1")