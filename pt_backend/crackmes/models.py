from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, DateTimeField, IntegerField, ForeignKey, CASCADE, IntegerChoices, \
    DateField, PositiveSmallIntegerField, BigAutoField, BooleanField
from django.utils.functional import cached_property

class AppUser(AbstractUser):
    @cached_property
    def solved_count(self):
        return len(list(ActionHistory.objects.filter(user=self, status=StatusEnum.SOLVED)))


class Task(Model):
    id = BigAutoField(primary_key=True)
    name = CharField(max_length=128)
    hexid = CharField(max_length=64)
    language = CharField(max_length=64, default='Unknown')
    date = DateField()
    writeups_num = IntegerField(default=0)
    comments_num = IntegerField(default=0)

    @cached_property
    def solutions(self):
        return ActionHistory.objects.filter(task_id=self.id).count()

    def __str__(self):
        return f'{self.name}'


class StatusEnum(IntegerChoices):
    CLEAR = 0, 'Clear'
    STARTED = 1, 'Started'
    ABORTED = 2, 'Aborted'
    SOLVED = 3, 'Solved'
    IGNORED = 4, 'Ignored'


class ActionHistory(Model):
    task = ForeignKey(Task, on_delete=CASCADE, related_name="actions")
    user = ForeignKey(AppUser, on_delete=CASCADE)
    status = PositiveSmallIntegerField(default=StatusEnum.CLEAR, choices=StatusEnum.choices)
    date = DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.task.name} - {self.get_status_display()} - {self.date.strftime("%Y/%m/%d %H:%M:%S")}'


class ScrapperHistory(Model):
    date = DateTimeField(auto_now_add=True, blank=True)
    total_scrapped = IntegerField(default=0)
    created = IntegerField(default=0)
    updated = IntegerField(default=0)
    deleted = IntegerField(default=0)
    success = BooleanField(default=False)

    def __str__(self):
        return f'{self.date.strftime("%Y/%m/%d %H:%M:%S")} total:{self.total_scrapped}'
