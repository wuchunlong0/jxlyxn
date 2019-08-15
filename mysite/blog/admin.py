from django.contrib import admin
from .models import Contacts

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):    
    list_display = ('id','name','email','tel','content','date','status')
