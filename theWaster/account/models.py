from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='userProfile')
    name = models.CharField(max_length=128) # 姓名
    sex = models.CharField(max_length=128) # 性別
    birthdate = models.DateField() # 生日
    introduction = models.TextField(blank=True, null=True) # *自我介紹
    lavel = models.IntegerField() # 經驗
    emailVerifyCode = models.CharField(max_length=128) # Email驗證碼
    isEmailVerified = models.BooleanField(default=False) # Email驗證
    def __str__(self):
        return self.name + '(' + self.user.username + ')'