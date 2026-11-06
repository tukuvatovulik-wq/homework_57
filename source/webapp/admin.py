from django.contrib import admin

from .models import Status, Task, Type


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "summary", "status", "created_at", "updated_at")
    list_filter = ("status", "types")
    search_fields = ("summary", "description")
    filter_horizontal = ("types",)
    readonly_fields = ("created_at", "updated_at")
