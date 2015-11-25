__author__ = 'baranbartu'

from client import CeleryClient


class ContextManager(object):
    _client = None
    # _dashboard and _tasks are mutable and same object for each instance
    # so one instance will be used on the scope always
    _dashboard = {}
    _events = []

    def __init__(self, client=None):
        self._client = client or CeleryClient()

    @property
    def dashboard(self):
        self._dashboard['workers'] = self.workers()
        self._dashboard['registered_tasks'] = self.registered_tasks()
        self._dashboard['queue_tasks'] = self.queue_tasks()
        return self._dashboard

    @property
    def tasks(self):
        _tasks = []
        for event in self._events:
            task = {'name': event['name'], 'uuid': event['uuid'],
                    'state': event['type'].replace('task-', '').upper(),
                    'args': event['args'], 'kwargs': event['kwargs'],
                    'received': event['local_received']}
            _tasks.append(task)
        return _tasks

    def add_event(self, event):
        self._events.append(event)

    def workers(self):
        return self._client.workers()

    def registered_tasks(self):
        return self._client.registered_tasks()

    def queue_tasks(self):
        return {'active': self._client.active_tasks(),
                'reserved': self._client.reserved_tasks()}
