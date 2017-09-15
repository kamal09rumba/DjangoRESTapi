from django.contrib import admin

# Register your models here.
from models import Todo
class TodoAdmin(admin.ModelAdmin):
    list_display = ["__str__","completed"]
    class Meta:
        model = Todo

admin.site.register(Todo,TodoAdmin)