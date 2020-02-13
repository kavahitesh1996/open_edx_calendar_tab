from django.conf.urls import url

from .views import calendar_dashboard, calendar_edit

urlpatterns = (
    url(r"^$", calendar_dashboard, name="calendar_dashboard"),
    url(r"^edit/$", calendar_edit, name="calendar_edit"),
)
