from django.contrib import admin
from website.models import user,myuploadfiles

# Register your models here.
class showadmin(admin.ModelAdmin):
        list_display = ('myfiles','datetime')
admin.site.register(myuploadfiles,showadmin)    



# class showuser(admin.ModelAdmin):
#         list_display2 = ('email','username')
# admin.site.register(user)
