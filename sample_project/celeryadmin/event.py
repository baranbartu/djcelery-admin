__author__ = 'baranbartu'
import threading


class EventListener(threading.Thread):
    def __init__(self, app=None):
        threading.Thread.__init__(self)
        self.daemon = True
