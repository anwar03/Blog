from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser):
        """Creates and saves a user with the giver email and password."""

        now = timezone.now()

        if not email:
            raise ValueError('The given email must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, is_active=True, is_staff=is_staff,
                         is_superuser=is_superuser, last_login=now, date_joined=now)
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    
    def create_user(self, email,  password=None):
        return self._create_user(email, password, False, False)
    

    def create_superuser(self, email, password):
        return self._create_user(email, password, True, True)

