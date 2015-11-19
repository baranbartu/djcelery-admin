__author__ = 'baranbartu'

from client import CeleryClient


class Context(object):
    client = None
    _dashboard = {}

    def __init__(self):
        self.client = CeleryClient()

    @property
    def dashboard(self):
        self._dashboard['workers'] = self.workers()
        return self._dashboard

    def workers(self):
        result = self.client.workers()
        return result
