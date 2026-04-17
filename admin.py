from django.contrib import admin
from testapp.models import employee

# Register your models here.
class empadmin(admin.ModelAdmin):
    list_display=['id','eno','ename','esal','eaddr']
admin.site.register(employee,empadmin)