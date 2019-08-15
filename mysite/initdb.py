# -*- coding: UTF-8 -*-
import os
import sys
import django
import random
import datetime


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    django.setup()
    from django.contrib.auth.models import User, Group, Permission

    
    User.objects.create_superuser('admin', 'admin@test.com','1234qazx')
    User.objects.create_superuser('ceo', 'ceo@ceo.com','ceoceo')

    #test 默认  user.is_staff = False  user.is_superuser = False  #不能从后台登录
    User.objects.create_user('test', 'test@test.com','1234qazx') 
 

 
    
 