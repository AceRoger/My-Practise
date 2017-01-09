from django.conf.urls import include, url
from blog import views


urlpatterns = [
    url(r'^$', views.test,name='test'),
    url(r'^get-data/', views.get_data, name='get_data'),
]

