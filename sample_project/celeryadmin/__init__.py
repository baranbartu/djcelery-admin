from client import CeleryClient
from context import ContextManager
from events import EventListener

celery_client = CeleryClient()
context_manager = ContextManager(client=celery_client)
event_listener = EventListener(celery_client, context_manager)
event_listener.start()
