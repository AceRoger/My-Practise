from django.shortcuts import render
from django.http import HttpResponse
import json
from django.core.serializers.json import DjangoJSONEncoder

from tasks import count_incr


from .models import t_one

# Create your views here.

def test(request):
	return render(request,'blog/blog.html')	

def get_data(request):
	print "In get_data View"
	# try:
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
	

	# print "view data = ",data
	# return HttpResponse(json.dumps(data), content_type='application/json')
	count_incr()
	return True

	# except Exception, e:
	# print "Exception = ",e
		# return HttpResponse(json.dumps(data), content_type='application/json')
	
	
	
