__author__ = 'baranbartu'

from client import CeleryClient


class ContextManager(object):
    client = None
    _dashboard = {}

    def __init__(self):
        self.client = CeleryClient()

    @property
    def dashboard(self):
        self._dashboard['workers'] = self.workers()
        self._dashboard['registered_tasks'] = self.registered_tasks()
        return self._dashboard

    def workers(self):
        return self.client.workers()

    def registered_tasks(self):
        return self.client.registered_tasks()
