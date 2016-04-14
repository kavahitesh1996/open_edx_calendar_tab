Calendar tab

add in `lms/urls.py`

<pre>
url(
    r'^courses/{}/calendar/'.format(
        settings.COURSE_ID_PATTERN,
    ),
    include('calendar_tab.urls'),
    name='calendar_endpoints',
),
</pre>

add in `ADDL_INSTALLED_APPS` `'calendar_tab'`
