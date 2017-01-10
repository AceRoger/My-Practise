from django.conf.urls import include, url
from django.contrib import admin
from blog import urls as blog

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include(blog, namespace='blog')),
]


