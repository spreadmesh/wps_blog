from django.conf.urls import url, include

from wpsblog.views import *


policy_urlpatterns = [
        url(r'terms/$', terms, name="terms"),
        url(r'privacy/$', privacy, name="privacy"),
        url(r'disclaimer/$', disclaimer, name="disclaimer"),
    ]

