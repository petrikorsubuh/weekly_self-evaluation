from django.db import models
from django.contrib.auth.models import User
class Categories(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='users')
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'

class Target(models.Model):
    categories = models.ForeignKey(Categories,on_delete=models.CASCADE,related_name='category')
    activity = models.CharField(max_length=45)
    target_set = models.IntegerField()
    unit = models.CharField(max_length=15)
    

    def __str__(self):
        return self.activity

    class Meta:
        db_table = 'target'
        ordering =['categories']
