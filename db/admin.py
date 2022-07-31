from django.contrib import admin
from db.models import Exercise


class ExerciseAdmin(admin.ModelAdmin):

    list_display = ['title', 'time_create', 'author']


admin.site.register(Exercise, ExerciseAdmin)