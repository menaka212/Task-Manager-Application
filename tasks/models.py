from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):

    PRIORITY_CHOICES = (
        ('High','High'),
        ('Medium','Medium'),
        ('Low','Low'),
    )

    STAGE_CHOICES = (
        ('todo','Todo'),
        ('progress','In Progress'),
        ('done','Done'),
    )

    user = models.ForeignKey(User,on_delete=models.CASCADE)

    title = models.CharField(max_length=100)

    description = models.TextField()

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='Medium'
    )

    stage = models.CharField(
        max_length=20,
        choices=STAGE_CHOICES,
        default='todo'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )