# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from userena.models import UserenaLanguageBaseProfile


class UserProfile(UserenaLanguageBaseProfile):
    user = models.OneToOneField(User)

    class Meta:
        app_label = 'auth'
        verbose_name = u'User profile'
        verbose_name_plural = u'User profiles'
