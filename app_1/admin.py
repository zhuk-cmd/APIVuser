from django.contrib import admin

# Register your models here.
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    model = Employee
    list_display = ('name','position','date','earnings','inform','parent')
    list_display_links = ('name','parent')
    list_filter = ('position','parent')
    actions = ['fast_delete']
    @admin.action(description='Удалить информацию о выплаченой зп сотрудников')
    def fast_delete(self,request,queryset):
        super().delete_model(request,Employee.inform)
        #Employee.objects.filter(inform=request.POST).delete()
        #queryset.delete(inform)
        #Employee.delete()
        # many.delete()

admin.site.register(Employee, EmployeeAdmin)


# class EmployeeAdmin(admin.ModelAdmin):
#      list_filter = ('is_staff','position')
