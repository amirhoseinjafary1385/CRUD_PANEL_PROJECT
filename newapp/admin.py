from django.contrib import admin
from .models import Member

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_show = "firstname", "lastname", "country" #, "email"
    
    
admin.site.register(Member, MemberAdmin)

