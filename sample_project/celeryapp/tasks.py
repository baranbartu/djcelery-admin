from __future__ import absolute_import

import time
from celery import shared_task


@shared_task
def test_task():
    time.sleep(20)
    return 'Completed'
