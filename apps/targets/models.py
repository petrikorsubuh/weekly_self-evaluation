from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'

class Target(models.Model):
    categories = models.ForeignKey(Categories,on_delete=models.CASCADE,related_name='categories')
    activity = models.CharField(max_length=45)
    target_set = models.CharField(max_length=4)
    unit = models.CharField(max_length=15)
    

    def __str__(self):
        return self.activity

    class Meta:
        db_table = 'target'
        ordering =['categories']
