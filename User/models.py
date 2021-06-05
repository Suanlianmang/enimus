from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

CHOICE = (('customer', 'customer'), ('seller', 'seller'), ('staff', 'staff'))

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    verified = models.BooleanField(default=False)
    user_type = models.CharField(max_length=30, choices=CHOICE)

class Address(models.Model):
    pincode = models.CharField(max_length=10)
    town_city = models.CharField(max_length=30)
    address = models.CharField(max_length=150)
    landmark = models.CharField(max_length=150)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
