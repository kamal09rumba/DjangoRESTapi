from django.conf.urls import url, include
from django.contrib import admin
import todos

urlpatterns = [
     url(r'^admin/', admin.site.urls),
     url(r'^', include('invoices.urls')),
     url(r'^todos/', include('todos.urls')),
     url(r'^accounts/login/$', todos.views.login, name='login'),
     url(r'^accounts/auth/$', todos.views.auth_view, name='auth_view'),
     url(r'^accounts/logout/$', todos.views.logout, name='logout'),
     url(r'^accounts/loggedin/$',todos.views.loggedin, name='loggedin'),
     url(r'^accounts/invalid/$', todos.views.invalid_login, name='invalid_login'),

]
