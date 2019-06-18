from jet.dashboard.modules import DashboardModule

from management.models import Activity, Person


class ActivityStudent(DashboardModule):
    title = 'Numero de Estudiantes por Actividad'
    template = 'modules/activity_student.html'

    def init_with_context(self, context):
        import json
        data = [{'label': activity.title, 'value': activity.number_of_students}
                for activity in context['user'].activities.all()]
        self.data = json.dumps(data)
