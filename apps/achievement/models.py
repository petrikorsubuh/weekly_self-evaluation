from django.db import models
from django.contrib.auth.models import User
from apps.targets.models import Target

class Achievement(models.Model):
    target = models.ForeignKey(Target, on_delete=models.CASCADE, related_name='item')
    category  = models.CharField(max_length=25)
    activity = models.CharField(max_length=45)
    target_set = models.IntegerField()
    unit = models.CharField(max_length=15)
    actual = models.IntegerField()
    date = models.DateField()
    def __str__(self):
        return self.activity

    class Meta:
        db_table = 'achievement'
        ordering = ['date','category']

