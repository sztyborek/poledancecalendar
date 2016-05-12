from __future__ import unicode_literals

from django.db import models

class Event(models.Model):
    EVENT_STATUS_CHOICES = (
        ('n', 'new'),
        ('a', 'active'),
        ('r', 'rejected')
    )

    EVENT_CATEGORY_CHOICES = (
        ('w', 'workshop'),
        ('c', 'competition'),
        ('s', 'show')

    )

    date = date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=1,
        choices=EVENT_STATUS_CHOICES,
        default='n')
    facebook_event = models.CharField(max_length=150, blank=True)
    contact_mail = models.EmailField(max_length=150, blank=True)
    category = models.CharField(max_length=1,
        choices=EVENT_CATEGORY_CHOICES,
        blank=False,
        null=False)


