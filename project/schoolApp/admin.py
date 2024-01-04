from django.contrib import admin

from schoolApp.models import schoolApp
from schoolApp.models import Teacher1

class studentadmin(admin.ModelAdmin):
    list_display=['name','classname','fathername','contact']

class teacheradmin(admin.ModelAdmin):
    list_display=['name','subject','exp','contact']

# Register your models here.

admin.site.register(schoolApp)

admin.site.register(Teacher1)

