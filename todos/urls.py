from django.conf.urls import url,include
from todos import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^active/$',views.show_active,name='show_active'),
    url(r'^completed/$',views.show_completed,name='show_completed'),
    url(r'^clear_completed/$',views.clear_completed,name='clear_completed'),
    url(r'^save_state/$',views.save_state,name='save_state'),
    url(r'^search/$',views.search,name='search'),
    url(r'^language/(?P<language>[a-z\-]+)/$',views.language,name='language'),
]