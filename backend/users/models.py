from django.contrib.auth.models import AbstractUser
from django.db import models


def _get_image_directory_path(self, instance) -> str:
    # file will be uploaded to MEDIA_ROOT / user_<id>_<username>
    return f'user_{instance.user.id}_{instance.user.username}'


class GenderChoices(models.TextChoices):
    MALE = 'Male'
    FEMALE = 'female'


class User(AbstractUser):
    middle_initial = models.CharField(null=True, max_length=250)
    birthday = models.DateField(null=True, blank=False)
    phone = models.CharField(null=True, max_length=50)
    gender = models.CharField(choices=GenderChoices.choices, max_length=50, null=True, blank=False)
    country = models.CharField(null=False, blank=False, max_length=100, default='Russia')  # TODO: create choices
    region = models.CharField(null=True, max_length=250)
    city = models.CharField(null=True, max_length=250)
    address_line = models.TextField(null=True)
    image = models.URLField(null=True)  # TODO: create like in other project
    # image = ImageField(upload_to=_get_image_directory_path)

    @property
    def get_user_full_name(self) -> str:
        if self.middle_initial is None:
            return self.get_full_name()
        return f'{self.last_name} {self.first_name} {self.middle_initial}'
