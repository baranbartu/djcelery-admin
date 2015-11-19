__author__ = 'baranbartu'

from django.conf import settings
from celery.app.control import Control
from utils import import_object


class CeleryClient(object):
    application = None
    control = None

    def __init__(self):
        path = getattr(settings, 'CELERY_APPLICATION_PATH', None)
        if path is None:
            raise ValueError(
                'You need to define "CELERY_APPLICATION_PATH" on settings.')
        self.application = import_object(path)
        self.control = Control(self.application)

    def workers(self):
        """
        get worker statuses
        :return:
        """
        response = self.control.ping()
        workers = []
        for w in response:
            worker = {}
            for k, v in w.iteritems():
                worker['id'] = k
                for k_inner, v_inner in v.iteritems():
                    if k_inner == 'ok' and v_inner == 'pong':
                        worker['up'] = True
                    else:
                        worker['up'] = False
                    break
                workers.append(worker)

        return workers

    def registered_tasks(self):
        """
        get registered task list
        :return:
        """
        response = self.control.inspect().registered()
        registered_tasks = {}
        for worker, tasks in response.iteritems():
            for task in tasks:
                if task in registered_tasks:
                    exists = registered_tasks[task]
                    registered_tasks[task] = list(set(exists.append(worker)))
                else:
                    registered_tasks[task] = [worker]

        return registered_tasks
