from django.contrib import admin
from db.models import Exercise, Articles


class ExerciseAdmin(admin.ModelAdmin):

    list_display = ['title', 'time_create', 'author']


class ArticlesAdmin(admin.ModelAdmin):

    list_display = ['title', 'time_create', 'author']


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Articles, ArticlesAdmin)
