from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='userProfile')
    name = models.CharField(max_length=128) # 姓名
    sex = models.CharField(max_length=128) # 性別
    birthdate = models.DateField(null=True, blank=True) # 生日
    introduction = models.TextField() #自我介紹
    lavel = models.IntegerField() #經驗
    
    def __str__(self):
        return self.name + '(' + self.user.username + ')'