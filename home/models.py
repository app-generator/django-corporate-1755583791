# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Employee(models.Model):

    #__Employee_FIELDS__
    fio = models.TextField(max_length=255, null=True, blank=True)
    pl = models.TextField(max_length=255, null=True, blank=True)
    salary = models.TextField(max_length=255, null=True, blank=True)

    #__Employee_FIELDS__END

    class Meta:
        verbose_name        = _("Employee")
        verbose_name_plural = _("Employee")


class Инциденты(models.Model):

    #__Инциденты_FIELDS__
    date start = models.DateTimeField(blank=True, null=True, default=timezone.now)
    data end = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Инциденты_FIELDS__END

    class Meta:
        verbose_name        = _("Инциденты")
        verbose_name_plural = _("Инциденты")


class Ticket(models.Model):

    #__Ticket_FIELDS__
    description = models.TextField(max_length=255, null=True, blank=True)
    title = models.TextField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)

    #__Ticket_FIELDS__END

    class Meta:
        verbose_name        = _("Ticket")
        verbose_name_plural = _("Ticket")



#__MODELS__END
