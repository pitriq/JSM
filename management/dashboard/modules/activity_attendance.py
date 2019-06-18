from jet.dashboard.modules import DashboardModule

from accounts.models import User
from management.models import Activity, Assistance


class ActivityAttendance(DashboardModule):
    title = 'Asistencia de actividades'
    q = 3
    subtitle = f'Promedio de asistencia de actividades (Porcentaje últ. {q} clases)'
    template = 'modules/activity_attendance.html'

    def init_with_context(self, context):
        import json

        user = context.request.user
        activities = Activity.objects.filter(teacher__in=[user])
        attendance_data = []
        activity_labels = []

        for activity in activities:
            percentage = 0
            total_enrolled = activity.student.count()
            assistances = Assistance.objects.filter(
                activity=activity).order_by('-date')[:self.q]
            for a in assistances:
                attendance = a.assistance.count()
                percentage += (attendance * 100.0) / total_enrolled
            attendance_data.append({
                'title': activity.title,
                'attendance': percentage / self.q,
            })
            activity_labels.append(activity.title)

        self.data = json.dumps(attendance_data)
        self.activities = activity_labels
        print(self.activities)
