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
    print "IN get-data"
    # try:
    #     count = t_one.objects.all().count()
    # 	num = t_one.objects.all()[count-1].no
    # 	# for n in num:
    # 	# 	print "No = ",n.no
    # 	incr_no = num + 1
    #
    # 	num2 = t_one(
    # 	no = incr_no
    # 	)
    # 	print "Incremented No = ",incr_no
    #
    # 	no_data = {
    # 		'num':incr_no,
    # 	}
    # 	num2.save()
    #
    #     return True
    # except Exception,e:
    #     print "Exception = ", e
    #     return

    try:
        count_incr.delay()
        # Demo Change for branch demo
        a = 9 + 9
    except Exception, e:
        print "Exception = ",e
    return
