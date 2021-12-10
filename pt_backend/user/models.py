from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.utils.functional import cached_property



class AppUser(AbstractUser):
    username = CharField(
        'username',
        max_length=30,
        unique=True,
        help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',
        validators=[AbstractUser.username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )

    @cached_property
    def solved_count(self):
        from crackmes.models import ActionHistory, StatusEnum

        return len(list(ActionHistory.objects.filter(user=self, status=StatusEnum.SOLVED)))

