#!/usr/bin/env python

from TorBrowser import TorBrowser
import time

tor = TorBrowser(password="password")
tor.connect()


for i in range(10):
    
    # Your code ...

    # renew tor session
    tor.renew()
    time.sleep(5)

    print(tor.get_ip())
