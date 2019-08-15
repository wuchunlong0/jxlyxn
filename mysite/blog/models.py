from django.db import models

# Create your models here.
#联系我们
class Contacts(models.Model):
    name = models.CharField(max_length=12,blank=True, null=True) #留言人
    email = models.CharField(max_length=24,blank=True, null=True)
    tel = models.CharField(max_length=16,blank=True, null=True)
    content = models.TextField(max_length=256,blank=True, null=True)
    date = models.DateTimeField(auto_now=True, null=True, blank=True) #自动创建日期含时间
    status = models.IntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return self.name