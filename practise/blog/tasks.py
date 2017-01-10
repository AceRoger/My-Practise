
from celery.decorators import task
from .models import t_one
import dateutil.relativedelta
from datetime import timedelta
import datetime

@task()
def count_incr():
    print "Task is running..."
    return