from django.contrib import admin

from heroes3maps.models import ActionHistory, Map


class MapAdmin(admin.ModelAdmin):
    list_display = ("name", "heroes_version", "link")


class ActionHistoryAdmin(admin.ModelAdmin):
    def history_date(self, obj: ActionHistory):
        return obj.date.strftime("%Y/%m/%d %H:%M:%S")

    list_display = ("user", "map", "status", "history_date")


admin.site.register(Map, MapAdmin)
admin.site.register(ActionHistory, ActionHistoryAdmin)
