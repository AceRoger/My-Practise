import django
from django.db import models
from django.utils import timezone


# Create your models here.


class t_one(models.Model):
    no = models.IntegerField(blank=True,null=True)

    def __unicode__(self):
        return unicode(self.no)

