from django.db import models
from django.contrib.auth import get_user_model

from django.db.models.signals import post_save

from notifications.signals import notify

User = get_user_model()


# Create your models here.
class Badassness(models.Model):
    score = models.PositiveIntegerField(default=0)
    level = models.PositiveSmallIntegerField(default=1)
    user = models.OneToOneField(User, on_delete=models.CASCADE, 
                                related_name='reputation', primary_key=True)

    def __str__(self):
        return str(f"{self.user}: {self.score}, level: {self.level}")


def my_notifier(sender, instance, created, **kwargs):
    if created:
        notify.send(sender=instance.user,
                    verb=f"New Badass ({instance.user}) created!", 
                    recipient=instance.user 
                    )


post_save.connect(my_notifier, sender=Badassness)