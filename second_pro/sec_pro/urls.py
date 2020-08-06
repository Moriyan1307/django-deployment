from django.conf.urls import url
from sec_pro import views

app_name = 'sec_pro'


urlpatterns = [
    # url(r'^$',views.index,name='index'),
    url(r'^other/$',views.other,name='other'),
    url(r'^relative/$',views.relative,name='relative')
]
 