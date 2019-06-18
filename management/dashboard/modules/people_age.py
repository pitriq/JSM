from jet.dashboard.modules import DashboardModule

from management.models import Person


class PeopleAge(DashboardModule):
    title = 'Edades de asistentes'
    template = 'modules/people_age.html'

    def init_with_context(self, context):
        from collections import Counter
        import json
        ages = [person.age for person in Person.objects.all()]
        self.data = json.dumps([{'label': str(k), 'value': v}
                                for k, v in Counter(ages).items()])
