from django.db import models

class Settings(models.Model):
    set_property = models.CharField(max_length=25)
    value = models.CharField(max_length=225)

    def __str__(self):
        return self.set_property

    class Meta:
        db_table = 'setting'

