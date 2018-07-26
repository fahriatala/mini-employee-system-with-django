from django.contrib import admin
from worker.models import *
# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
	list_display = ['name','information']
	list_filter = ()
	search_fields = ['name','information']
	list_per_page = 20

admin.site.register(Department,DepartmentAdmin)

class PositionAdmin(admin.ModelAdmin):
	list_display = ['name','information']
	list_filter = ()
	search_fields = ['name','information']
	list_per_page = 20

admin.site.register(Position,PositionAdmin)

class WorkerAdmin(admin.ModelAdmin):
	list_display=['name','address','gender_type','worker_type','position','department','email','phonenumber']
	list_filter = ('gender_type', 'worker_type', 'position', 'department')
  	search_fields = ['name', 'address', 'email', 'phonenumber']
 	list_per_page = 20

admin.site.register(Worker, WorkerAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display = ['account', 'worker', 'account_type']
    list_filter = ('account_type',)
    search_fields = []
    list_per_page = 20

admin.site.register(Account, AccountAdmin)

