from django.contrib import admin

from games.models import ActionHistory, Game


class GameAdmin(admin.ModelAdmin):
    list_display = ("name",)


class ActionHistoryAdmin(admin.ModelAdmin):
    def history_date(self, obj: ActionHistory):
        return obj.date.strftime("%Y/%m/%d %H:%M:%S")

    list_display = ("user", "game", "status", "history_date")


admin.site.register(Game, GameAdmin)
admin.site.register(ActionHistory, ActionHistoryAdmin)
