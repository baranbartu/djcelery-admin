__author__ = 'baranbartu'

from django.conf import settings
from celery.app.control import Control
from utils import import_object, nested_method


class CeleryClient(object):
    _application = None
    _control = None

    def __init__(self):
        path = getattr(settings, 'CELERY_APPLICATION_PATH', None)
        if path is None:
            raise ValueError(
                'You need to define "CELERY_APPLICATION_PATH" on settings.')
        self._application = import_object(path)
        self._control = Control(self._application)

    def get_application(self):
        return self._application

    def enable_events(self):
        self._control.enable_events()

    def disable_events(self):
        self._control.disable_events()

    def workers(self):
        response = self._control.inspect().stats()
        if not response:
            return []
        statuses = self.worker_statuses()
        workers = []
        for name, info in response.iteritems():
            worker = dict()
            worker['name'] = name
            worker['status'] = statuses[worker['name']]
            worker['concurrency'] = info['pool']['max-concurrency']
            worker['broker'] = {'transport': info['broker']['transport'],
                                'hostname': info['broker']['hostname'],
                                'port': info['broker']['port']}
            workers.append(worker)
        return workers

    def worker_statuses(self):
        """
        get worker statuses
        :return:
        """
        response = self._control.ping()
        workers = {}
        for w in response:
            for k, v in w.iteritems():
                for k_inner, v_inner in v.iteritems():
                    if k_inner == 'ok' and v_inner == 'pong':
                        workers[k] = 'Active'
                    else:
                        workers[k] = 'Passive'
                    break
        return workers

    def registered_tasks(self):
        """
        get registered task list
        :return:
        """
        response = self._control.inspect().registered()
        if not response:
            return []
        registered_tasks = {}
        for worker, tasks in response.iteritems():
            for task in tasks:
                if task in registered_tasks:
                    exists = registered_tasks[task]
                    exists.append(worker)
                    registered_tasks[task] = list(set(exists))
                else:
                    registered_tasks[task] = [worker]

        return registered_tasks

    def active_tasks(self):
        """
        get active tasks which is running currently
        :return:
        """
        response = self._control.inspect().active()
        if not response:
            return []
        tasks = []
        for worker, task_list in response.iteritems():
            for task in task_list:
                t = dict()
                t['queue'] = task['delivery_info']['routing_key']
                t['name'] = task['name']
                t['id'] = task['id']
                t['worker'] = worker
                tasks.append(t)
        return tasks

    def reserved_tasks(self):
        """
        get reserved tasks which is in queue but still waiting to be executed
        :return:
        """

        response = self._control.inspect().reserved()
        if not response:
            return []
        tasks = []
        for worker, task_list in response.iteritems():
            for task in task_list:
                t = dict()
                t['queue'] = task['delivery_info']['routing_key']
                t['name'] = task['name']
                t['id'] = task['id']
                t['worker'] = worker
                tasks.append(t)
        return tasks

    def run(self, command, parameter):

        def execute(*args):
            task_verbose = args[1]
            task = import_object(task_verbose)
            task.delay()

        def revoke(*args):
            ctrl = args[0]
            task_id = args[1]
            ctrl.revoke(task_id, terminate=True, signal="SIGKILL")

        control = self._control
        nested = nested_method(self, 'run', command)
        return nested(*(control, parameter))
