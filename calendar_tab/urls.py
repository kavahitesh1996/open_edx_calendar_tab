from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from .views import calendar_dashboard, calendar_edit

urlpatterns = patterns('',
    url(r"^$", login_required(calendar_dashboard), name="calendar_dashboard"),
    url(r"^edit/$", login_required(calendar_edit), name="calendar_edit"),
)
