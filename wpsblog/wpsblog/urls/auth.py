from django.conf.urls import url

from wpsblog.views.auth import *


urlpatterns = [
    url(r'^login/$', login, name="login"),
    url(r'^signup/$', signup, name="signup"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^mypage/$', mypage, name="mypage"),
]
