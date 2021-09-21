from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from crackmes.models import AppUser, Task, ActionHistory, ScrapperHistory

class ScrapperHistoryAdmin(admin.ModelAdmin):
    def history_date(self, obj: ScrapperHistory):
        return obj.date.strftime("%Y/%m/%d %H:%M:%S")

    list_display = ('history_date', 'total_scrapped', 'created', 'updated', 'deleted', 'success')


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'language', 'date', 'writeups_num', 'comments_num')


class ActionHistoryAdmin(admin.ModelAdmin):
    def history_date(self, obj: ScrapperHistory):
        return obj.date.strftime("%Y/%m/%d %H:%M:%S")

    list_display = ('user', 'task', 'status', 'history_date')


admin.site.register(AppUser, UserAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(ActionHistory, ActionHistoryAdmin)
admin.site.register(ScrapperHistory, ScrapperHistoryAdmin)
