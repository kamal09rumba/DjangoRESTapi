from django.conf.urls import url,include
from todos import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
]