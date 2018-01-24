#!/usr/bin/env python

from TorBrowser import TorBrowser
import time
from pyquery import PyQuery as pq
from lxml import etree
import requests
import re
import urllib.parse
import ast
import sys

tor = TorBrowser(password="password")
tor.connect()


for i in range(10):
    
    # Your code ...

    # renew tor session
    tor.renew()
    time.sleep(5)

    print(tor.get_ip())
