from django.utils.translation import ugettext_noop
from courseware.tabs import CourseTab


class CalendarTab(CourseTab):

    name = "calendar_tab"
    title = ugettext_noop("Calendar")
    view_name = "calendar_dashboard"
    tab_id = "calendar_tab"
    type = 'calendar_tab'
    is_hideable = True
    is_default = True
    is_dynamic = False
    data = '{}'

    def __init__(self, tab_dict=None):
        self.data = tab_dict.get('data') if tab_dict else '{}'

        if tab_dict is None:
            tab_dict = dict()

        super(CalendarTab, self).__init__(tab_dict)

    def __getitem__(self, key):
        if key == 'data':
            return self.data
        else:
            return super(CalendarTab, self).__getitem__(key)

    def __setitem__(self, key, value):
        if key == 'data':
            self.data = value
        else:
            super(CalendarTab, self).__setitem__(key, value)

    @classmethod
    def is_enabled(cls, course, user=None):
        return True

    @classmethod
    def validate(cls, tab_dict, raise_error=True):
        return True

    def to_json(self):
        """ Return a dictionary representation of this tab. """
        to_json_val = super(CalendarTab, self).to_json()
        to_json_val.update({'data': self.data})
        return to_json_val
