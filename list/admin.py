from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ExportMixin

class TodoResource(resources.ModelResource):

	class Meta:
		model = Todo
		fields = ('id','time_created','title','description','status')
		export_order = ('id', 'time_created','title','description','status')

class TodoAdmin(ExportMixin,admin.ModelAdmin):
	resource_class = TodoResource
	list_display = ('id','time_created','title','description','status')
	search_fields = ('title','time_created','status')



admin.site.register(Todo,TodoAdmin)

# Register your models here.
