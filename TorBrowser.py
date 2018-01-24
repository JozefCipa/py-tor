import requests
import socket
import socks
from stem import Signal
from stem.control import Controller


class TorBrowser:

    def __init__(self, password, port=9151):
        try:
            self._controller = Controller.from_port(port=port)
            self._controller.authenticate(password)
        except Exception:
            print("""Couldn\'t connect to Tor Browser. \
Please, make sure it\'s started.""")
            exit(-1)

    def connect(self, port=9150, ip="127.0.0.1"):
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, ip, port, True)
        socket.socket = socks.socksocket

    def renew(self):
        self._controller.signal(Signal.NEWNYM)

    def get_ip(self):
        req = requests.Session()
        res = req.get("http://checkip.amazonaws.com/")

        return res.text
