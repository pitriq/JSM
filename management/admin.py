from django.contrib import admin

from ._admin.activity import *
from ._admin.assistance import *
from ._admin.dwelling import *
from ._admin.income import *
from ._admin.person import *

# Register your models here.
admin.site.site_header = 'Adminitración de JSM'
