from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length = 30, blank = False, unique = True)
    created_at = models.DateTimeField( auto_now_add = timezone.now() )
    updated_at = models.DateTimeField( auto_now_add = True )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
    
