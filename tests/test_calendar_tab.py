from courseware.tests.test_tabs import TabTestCase
from calendar_tab.tab import CalendarTab


class CalendarTabTestCase(TabTestCase):
    """Test cases for Calendar Tab."""

    def test_calendar_tab(self):

        tab = self.check_tab(
            tab_class=CalendarTab,
            dict_tab={'type': CalendarTab.type, 'name': 'same', 'data': '{}'},
            expected_link=self.reverse(CalendarTab.view_name, args=[self.course.id.to_deprecated_string()]),
            expected_tab_id=CalendarTab.tab_id,
            invalid_dict_tab=None,
        )
        self.check_can_display_results(tab)
        self.check_get_and_set_method_for_key(tab, 'data')
