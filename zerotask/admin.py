from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('msg', 'created', 'finish_ts', 'status', 'queue')


admin.site.register(Task, TaskAdmin)
