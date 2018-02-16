from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

import logging

from .managers import UserManager
# Create your models here.

logger = logging.getLogger(__name__)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=10)
    
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)
    country = models.CharField(max_length=2, default='bn', db_index=True)
    

    objects = UserManager()

    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['name']
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    
    def __unicode__(self):

        return u"Email: {}".format(self.email)


    def __str__(self):
        """Django uses this when it needs to convert the object to a string."""
        
        return self.email

    
    def get_full_name(self):
        """Return the user full name."""
        name = u"{} {}".format(self.first_name, self.last_name)
        return name.strip()

    
    def get_short_name(self):
        """Return the user short name."""
        
        return u"{}".format(self.email)
    

class UserFeed(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns model as a to string."""

        return self.status_text
