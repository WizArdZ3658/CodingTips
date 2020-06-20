from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from datetime import date


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    country = CountryField(blank_label='(select country)')
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    dob = models.DateField(default=date.today())

    def __str__(self):
        return f'(self.user.username) Profile'

    # def save(self, *args, **kwargs):
    #     super().save()
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
