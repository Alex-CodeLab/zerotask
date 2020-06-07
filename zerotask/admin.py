from django.contrib import admin

# Register your models here.
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('msg', 'created','finish_ts','status', 'queue')


admin.site.register(Task, TaskAdmin)
