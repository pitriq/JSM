from django.db import models

from config.settings.development import AUTH_USER_MODEL


class Dwelling(models.Model):
    type = models.CharField('Tipo de vivienda', max_length=64)

    class Meta:
        verbose_name = 'Vivienda'
        verbose_name_plural = 'Viviendas'

    def __str__(self):
        return f'{self.type}'


class Income(models.Model):
    type = models.CharField('Tipo de ingreso', max_length=64)

    class Meta:
        verbose_name = 'Ingreso'
        verbose_name_plural = 'Ingresos'

    def __str__(self):
        return f'{self.type}'


class Person(models.Model):
    PRESCHOOL = SINGLE = 0
    PRIMARYSCHOOL = MARRIED = 1
    SECONDARYSCHOOL = DIVORCED = 2
    UNIVERSITY = WIDOWED = 3
    CIVIL_CHOICES = ((SINGLE, 'Soltero/a'), (MARRIED, 'Casado/a'),
                     (DIVORCED, 'Divorciado/a'), (WIDOWED, 'Viudo/a'))
    first_name = models.CharField('Nombre', max_length=128)
    last_name = models.CharField('Apellido', max_length=128)
    date_of_birth = models.DateField('Fecha de nacimiento')
    dni = models.IntegerField('DNI', unique=True)
    address = models.CharField(
        'Dirección',
        max_length=128,
        blank=True,
        null=True)
    civil_status = models.IntegerField(
        'Estado civil', default=0, choices=CIVIL_CHOICES)
    dwelling = models.ManyToManyField(
        Dwelling, blank=True, related_name='person')
    dwelling.verbose_name = 'Vivienda'
    income = models.ManyToManyField(
        Income, blank=True, related_name='person')
    income.verbose_name = 'Ingreso'
    is_working = models.BooleanField('Trabaja', default=False)
    work_place = models.CharField(
        'Lugar de trabajo',
        max_length=128,
        blank=True,
        null=True)

    is_healthy = models.BooleanField('Problema de salud', default=False)
    which_issue = models.CharField(
        'Cual?',
        max_length=128,
        blank=True,
        null=True)
    is_medicated = models.BooleanField('Toma medicación', default=False)
    which_medicated = models.CharField(
        'Cual?',
        max_length=128,
        blank=True,
        null=True)

    STAGES_CHOICES = ((PRESCHOOL, 'Jardin'), (PRIMARYSCHOOL, 'Primaria'),
                      (SECONDARYSCHOOL, 'Secundario'), (UNIVERSITY, 'Universidad'))
    education_stage = models.IntegerField(
        'Nivel eductivo alcazado',
        default=0,
        choices=STAGES_CHOICES)
    dropout_reason = models.CharField(
        'Motivo de abandono',
        max_length=64,
        blank=True,
        null=True)

    religion = models.CharField(
        'Religion que practica',
        max_length=64,
        blank=True,
        null=True)
    is_baptized = models.BooleanField('Esta bautizado?', default=False)
    is_communion = models.BooleanField('Hijo la comunion ', default=False)
    is_confirmation = models.BooleanField(
        'Hizo la confirmacion', default=False)

    note = models.TextField('Observaciones', default='', blank=True, null=True)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Relative(models.Model):
    first_name = models.CharField('Nombre', max_length=128)
    last_name = models.CharField('Apellido', max_length=128)
    address = models.CharField(
        'Dirección',
        max_length=128,
        blank=True,
        null=True)


class ResponsibleFamily(Relative):
    FATHER = 0
    MOTHER = 0
    TUTOR = 0
    TYPE_CHOICES = ((FATHER, 'Padre'), (MOTHER, 'Madre'), (TUTOR, 'Tutor'))
    type = models.IntegerField('Familiar', default=0, choices=TYPE_CHOICES)
    is_alive = models.BooleanField('Esta vivo', default=True)
    work = models.CharField('Ocupación', max_length=64, blank=True, null=True)
    person = models.ForeignKey(
        Person,
        related_name='responsible_family',
        blank=True,
        null=True,
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Familiar responble'
        verbose_name_plural = 'Familiares responbles'

    def __str__(self):
        return f'{self.type} {self.first_name} {self.last_name}'


class Family(Relative):
    SIBLING = 0
    COUPLE = 1
    TYPE_CHOICES = ((COUPLE, 'Pareja'), (SIBLING, 'Hermano'),)
    type = models.IntegerField('Familiar', default=0, choices=TYPE_CHOICES)
    date_of_birth = models.DateField('Fecha de nacimiento')
    person = models.ForeignKey(
        Person,
        related_name='sibling',
        blank=True,
        null=True,
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Familia'
        verbose_name_plural = 'Familias'

    def __str__(self):
        return f'{self.type} {self.first_name} {self.last_name}'


class VCard(models.Model):
    PHONE = 'phone'
    EMAIL = 'email'
    TYPES_AVAILABLES = ((EMAIL, 'Email'), (PHONE, 'Teléfono'))
    type_of_card = models.CharField(
        "Tipo de dato",
        choices=TYPES_AVAILABLES,
        max_length=20)
    data = models.CharField("Valor", max_length=128)
    upload_date = models.DateTimeField('Last change', auto_now=True)
    user = models.ForeignKey(
        Person,
        related_name='vcards',
        null=True,
        blank=True,
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return f'{self.type_of_card} {self.data}'


class Son(models.Model):
    PRESCHOOL = 0
    PRIMARYSCHOOL = 1
    SECONDARYSCHOOL = 2
    parent = models.ForeignKey(
        Person,
        related_name='sons',
        on_delete=models.CASCADE,
        blank=True,
        null=True)
    first_name = models.CharField('Nombre', max_length=128)
    last_name = models.CharField('Apellido', max_length=128)
    date_of_birth = models.DateField('Fecha de nacimiento')
    STAGES_CHOICES = ((PRESCHOOL, 'Jardin'), (PRIMARYSCHOOL, 'Primaria'),
                      (SECONDARYSCHOOL, 'Secundario'))
    education_stage = models.IntegerField(
        'Nivel eductivo alcazado',
        default=0,
        choices=STAGES_CHOICES)

    class Meta:
        verbose_name = 'Hijo'
        verbose_name_plural = 'Hijos'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class DayOfWeek(models.Model):
    name = models.CharField('Dia de la semana', max_length=16, unique=True)

    class Meta:
        verbose_name = 'Dia de la semana'
        verbose_name = 'Dias de la semana'

    def __str__(self):
        return f'{self.name}'


class Activity(models.Model):
    title = models.CharField('Nombre de la actividad', max_length=128)
    teacher = models.ManyToManyField(
        AUTH_USER_MODEL, related_name='activities')
    teacher.verbose_name = 'Profesor'
    start_date = models.DateField('Comienzo de la actividad')
    end_date = models.DateField('Fin de la actividad')
    student = models.ManyToManyField(Person, related_name='activities')
    student.verbose_name = 'Inscriptos'

    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'

    def __str__(self):
        return f'{self.title}'


class Turn(models.Model):
    day_of_week = models.ForeignKey(
        DayOfWeek,
        related_name='activities',
        on_delete=models.CASCADE)
    day_of_week.verbose_name = 'Dia de la semana'
    start_time = models.TimeField('Hora de inicio de la actividad')
    end_time = models.TimeField('Hora de end de la actividad')
    activity = models.ForeignKey(
        Activity,
        related_name='turns',
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'

    def __str__(self):
        return f'{self.activity} {self.day_of_week} {self.start_time} {self.end_time}'


class Assistance(models.Model):
    date = models.DateField('Fecha', auto_now_add=True)
    activity = models.ForeignKey(
        Activity,
        related_name='courses',
        blank=True,
        null=True,
        on_delete=models.CASCADE)
    activity.verbose_name = 'Actividad'
    assistance = models.ManyToManyField(Person, related_name='courses')
    assistance.verbose_name = 'Quien esta presente?'

    class Meta:
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'

    def __str__(self):
        return f'{self.activity} {self.date}'
