from django.contrib.auth.models import User
from django.db import models


class Edition(models.Model):
    editionName = models.CharField(max_length=128) #版名
    user = models.ManyToManyField(User)  #板主

    def __str__(self):
        return self.editionName
    
    
class Article(models.Model):
    edition = models.ForeignKey(Edition) #版名
    user = models.ForeignKey(User) #發文者
    title = models.CharField(max_length=128) #標題
    content = models.TextField() #內容
    dateTime = models.DateTimeField() #發表時間
#    bad = models.ManyToManyField(User) #廢

    def __str__(self):
        return self.title


class badArticle(models.Model):
    edition = models.ForeignKey(Article)
    bad = models.ManyToManyField(User) #廢

class Comment(models.Model):
    article = models.ForeignKey(Article) 
    user =  models.ForeignKey(User) #留言者
    content = models.TextField() #內容
    dateTime = models.DateTimeField() #留言時間
#     bad = models.ManyToManyField(User) #廢

    def __str__(self):
        return self.content                
                



