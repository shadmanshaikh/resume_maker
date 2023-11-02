from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Tool,CodingSkill,Employee,Designation,Projects


admin.site.register(Tool)
admin.site.register(CodingSkill)
admin.site.register(Employee)
admin.site.register(Designation)
admin.site.register(Projects)


