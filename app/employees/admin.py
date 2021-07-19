from django.contrib import admin

from .models import Employee, Grade, Position

admin.site.register(Employee)
admin.site.register(Grade)
@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', 'pk')
