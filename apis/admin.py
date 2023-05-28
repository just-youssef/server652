from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

# Register your models here.
admin.site.site_header = "الكتيبة ٦٥٢ حرب إلكترونية"
admin.site.site_title = "الكتيبة ٦٥٢ حرب إلكترونية"
admin.site.index_title = "قاعدة بيانات الكتيبة"

admin.site.unregister(Group)


from django.contrib import admin

class جنودAdmin(admin.ModelAdmin):
    search_fields = ['اسم', 'رقم_عسكرى']

class ضباط_صفAdmin(admin.ModelAdmin):
    search_fields = ['اسم', 'رقم_عسكرى']

class ضباطAdmin(admin.ModelAdmin):
    search_fields = ['اسم', 'رقم_الأقدمية']

admin.site.register(جنود, جنودAdmin)
admin.site.register(ضباط, ضباطAdmin)
admin.site.register(ضباط_صف, ضباط_صفAdmin)