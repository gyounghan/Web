from django.contrib import admin
from .models import Person, User_Info

class PersonAdmin(admin.ModelAdmin):
    pass

class UserInfo(admin.ModelAdmin):
    pass

admin.site.register(Person, PersonAdmin)

admin.site.register(User_Info, UserInfo)
# Register your models here.
