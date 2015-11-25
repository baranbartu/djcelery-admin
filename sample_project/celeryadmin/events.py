from celery.events import EventReceiver

__author__ = 'baranbartu'
import threading


class EventListener(threading.Thread):
    def __init__(self, celery_client, context_manager):
        threading.Thread.__init__(self)
        self.daemon = True

        self.celery_client = celery_client
        self.context_manager = context_manager

    def start(self):
        threading.Thread.start(self)

    def run(self):
        application = self.celery_client.get_application()
        with application.connection() as conn:
            receiver = EventReceiver(conn,
                                     handlers={"*": self.on_event},
                                     app=application)

            receiver.capture(limit=None, timeout=None, wakeup=True)

    def on_event(self, event):
        print event['type']
        if event['type'].startswith('task-'):
            self.context_manager.add_event(event)
