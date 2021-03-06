from django.contrib.auth.models import User
from django.db import models

from account.models import UserProfile


class Sort(models.Model):
    sort = models.CharField(max_length=128) #類別
    disabled = models.BooleanField(default=False) #啟用停用
    
    def __str__(self):
        return self.sort

class Edition(models.Model):
    sort = models.ForeignKey(Sort) 
    edition = models.CharField(max_length=128) #版名
    user = models.ManyToManyField(User)  #板主
    disabled = models.BooleanField(default=False) #啟用停用

    def __str__(self):
        return self.edition
    
    
class Article(models.Model):
    edition = models.ForeignKey(Edition)
    user = models.ForeignKey(User, related_name='Po') #發文者
    title = models.CharField(max_length=128) #標題
    content = models.TextField() #內容
    dateTime = models.DateTimeField() #發表時間
    bad = models.ManyToManyField(User) #廢

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article) 
    user =   models.ForeignKey(User, related_name='PoC') #留言者
    content = models.TextField() #內容
    dateTime = models.DateTimeField() #留言時間
    bad = models.ManyToManyField(User) #廢

    def __str__(self):
        return self.content                
                



