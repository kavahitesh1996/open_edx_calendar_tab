import json
import os

from django.core.context_processors import csrf
from django.http import Http404
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.utils.translation import ugettext as _

from edxmako.shortcuts import render_to_response
from edxmako.paths import add_lookup
from opaque_keys.edx.keys import CourseKey
from xmodule.modulestore.django import modulestore
from xmodule.tabs import CourseTabList

from courseware.courses import get_course_with_access
from courseware.access import has_access


def calendar_dashboard(request, course_id):
    course_key = CourseKey.from_string(course_id)
    course = get_course_with_access(request.user, "load", course_key)
    add_lookup('main', os.path.join(os.path.dirname(os.path.dirname(__file__)), 'calendar_tab/templates'))
    csrf_token = csrf(request)['csrf_token']
    tab = CourseTabList.get_tab_by_id(course.tabs, "calendar_tab")
    is_staff = bool(has_access(request.user, 'staff', course))

    try:
        data = json.loads(tab.data)
    except (TypeError, ValueError):
        data = {}

    context = {
        "course": course,
        "csrf_token": csrf_token,
        'url': data.get('url', '#'),
        'message': data.get('message', _('Open calendar')),
        'is_staff': is_staff
    }
    return render_to_response("calendar_tab/calendar_tab.html", context)


@require_POST
def calendar_edit(request, course_id):
    url = request.POST.get('url', '')
    message = request.POST.get('message', '')

    course_key = CourseKey.from_string(course_id)
    course = get_course_with_access(request.user, "load", course_key)

    # Find the given tab in the course
    tab = CourseTabList.get_tab_by_id(course.tabs, "calendar_tab")

    if tab is None or not bool(has_access(request.user, 'staff', course)):
        raise Http404("Tab with id_locator calendar_tab does not exist.")

    data = {'url': url, 'message': message}
    tab.data = json.dumps(data)
    modulestore().update_item(course, request.user.id)
    return redirect('calendar_dashboard', course_id=course.id)
