from django.conf.urls import url,include
from todos import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^active/$',views.show_active,name='show_active'),
    url(r'^completed/$',views.show_completed,name='show_completed'),
    url(r'^clear/$',views.clear_completed,name='clear_completed'),
]