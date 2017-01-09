from celery.decorators import task
from celery.decorators import periodic_task
from .models import t_one
import dateutil.relativedelta
from datetime import timedelta
import datetime

# @periodic_task(run_every=datetime.timedelta(minutes=1),name="allocate_unbilled_consumers",ignore_result=True)
# @periodic_task(run_every=datetime.timedelta(seconds=5),name="count_incr")
@task()
def count_incr():
	# try:
	# 	print "In tasks.py"
	# 	count = t_one.objects.all().count()
	# 	num = t_one.objects.all()[count-1].no
	# 	# for n in num:
	# 	# 	print "No = ",n.no
	# 	incr_no = num + 1
		
	# 	num2 = t_one(
	# 	no = incr_no
	# 	)
	# 	print "Incremented No = ",incr_no

	# 	no_data = {
	# 		'num':incr_no,
	# 	}

	# 	num2.save()
	# 	data = {'success':'true','no_data':no_data}
	# 	return data
	# except Exception,e:
	# 	print "Exception | tasks.py | count_incr ",e
	# 	data = {'success':'false'}
	# 	return data

	print "Task is running"
	return