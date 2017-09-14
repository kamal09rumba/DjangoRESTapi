from django.conf.urls import url
#from django.contrib import admin
from invoices import views
urlpatterns = [
    url(r'^invoices/$', views.invoice_list),
    url(r'^invoices/(?P<pk>[0-9]+)/$', views.invoice_detail),
]
