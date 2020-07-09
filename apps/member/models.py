from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    GENDER = (
        ('L','MALE'),
        ('P','FEMALE'),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user')
    age = models.CharField(max_length=12)
    gender = models.CharField(max_length=1,choices=GENDER)
    photo = models.ImageField(upload_to='member/',blank=True,null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'members'
