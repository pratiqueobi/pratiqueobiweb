from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    localizacao = models.CharField(max_length=100, blank=True, default='')
    instituicao = models.CharField(max_length=100, blank=True, default='')
    data_nascimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return  self.user.username



@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
