from django.db.models.signals import post_save

from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Account

def userAccount(sender, instance, created, **kwargs):

    if created:
        # group = Group.objects.get(name='user')
        # instance.groups.add(group)

        Account.objects.create( user=instance, username=instance.username )

        print('Profile created')

post_save.connect(userAccount, sender=User)