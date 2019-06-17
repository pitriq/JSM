from django.utils.translation import ugettext_lazy as _
from jet.dashboard import modules
from jet.dashboard.dashboard import AppIndexDashboard, Dashboard


class CustomIndexDashboard(Dashboard):
    columns = 3

    def init_with_context(self, context):
        self.available_children.append(modules.LinkList)
        self.children.append(modules.AppList(
            _('Applications'),
            column=2,
            order=0
        ))
