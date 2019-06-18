from django.utils.translation import ugettext_lazy as _
from jet.dashboard import modules
from jet.dashboard.dashboard import AppIndexDashboard, Dashboard

from .modules.activity_attendance import ActivityAttendance
from .modules.activity_student import ActivityStudent
from .modules.people_age import PeopleAge


class CustomIndexDashboard(Dashboard):
    columns = 3

    def init_with_context(self, context):
        self.available_children.append(modules.LinkList)
        self.children.append(modules.AppList(
            _('Applications'),
            column=2,
            order=0
        ))
        self.children.append(ActivityStudent(column=0))
        self.children.append(PeopleAge(column=1))
        self.children.append(ActivityAttendance(column=0))
