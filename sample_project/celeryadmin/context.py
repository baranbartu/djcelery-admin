__author__ = 'baranbartu'

from client import CeleryClient


class Context(object):
    client = None
    _dashboard = {}

    def __init__(self):
        self.client = CeleryClient()

    @property
    def dashboard(self):
        workers = self.workers()
        self._dashboard.setdefault('workers', workers)
        return self._dashboard

    def workers(self):
        result = self.client.workers()
        return result
