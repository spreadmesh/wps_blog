from django.conf.urls import url

from wpsblog.views.posts import *


urlpatterns = [
    url(r'^$', list, name="list"),
    url(r'^new/$', new, name="new"),
    url(r'^create/$', create, name="create"),
    url(r'^(?P<post_id>\d+)/$', detail, name="detail"),
    url(r'^(?P<post_id>\d+)/edit/$', edit, name="edit"),
    url(r'^(?P<post_id>\d+)/update/$', update, name="update"),
    url(r'^(?P<post_id>\d+)/delete/$', delete, name="delete"),

    # Comments
    url(r'^(?P<post_id>\d+)/comments/create/$', comments_create, name="comments-create"),
    url(r'^(?P<post_id>\d+)/comments/(?P<comment_id>\d+)/edit/$', comments_edit, name="comments-edit"),
    url(r'^(?P<post_id>\d+)/comments/(?P<comment_id>\d+)/update/$', comments_update, name="comments-update"),
    url(r'^(?P<post_id>\d+)/comments/(?P<comment_id>\d+)/delete/$', comments_delete, name="comments-delete"),
]
