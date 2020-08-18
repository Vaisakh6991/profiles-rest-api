
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# for usermanager
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """ Help django work with out custom user model. """

    def create_user(self, email, name, password=None ):
        """ Creates a new user profile object """
        
        if not email:
            raise ValueError(' Users must have an email address ')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self.db)

        return user
    
    def create_superuser(self, email, name, password):
        """ Creates and saves a new super user """

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self.db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Resprests a user profile inside our system """

    email   = models.EmailField(max_length=255, unique=True)
    name    = models.CharField(max_length=255)
    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=False)
    
    objects = UserProfileManager()

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Used to get a users full name """
        return self.name
    
    def get_short_name(self):
        """ Used to get users short name """
        return self.name
    
    def __str__(self):
        """ Django uses this when it needs to convert the object in a string """
        return self.email
    