from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tag/(?P<tag_name>[A-z0-9]+)/$', views.questions_by_tag, name='questions_by_tag'),
    url(r'^question/(?P<question_id>[0-9]+)/$', views.question_detail, name='question_detail'),
    url(r'^hot/$', views.hot, name='hot'),
    url(r'^login/$', views.login, name='login'),
    url(r'^singup/$', views.singup, name='singup'),
    url(r'^ask/$', views.ask, name='ask'),
]
