from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery.task import periodic_task
from celery.schedules import crontab
from datetime import timedelta
from celery import shared_task


# @periodic_task(run_every=(timedelta(seconds=5)), name='my_first_task')
# def my_first_task():
#     print('This is first task')


@shared_task
def second_task():
    print('This is second task')

# @periodic_task(run_every=(crontab(minute='*/1')), name='my_first_task')
# def my_first_task():
#     print('This is first task')


# @shared_task
# def add(x, y):
#     return x + y
#
#
# @shared_task
# def mul(x, y):
#     return x * y
#
#
# @shared_task
# def xsum(numbers):
#     return sum(numbers)
