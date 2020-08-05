from django.contrib import admin
from .models import Note


class NoteAdmin(admin.ModelAdmin):
    fields = ('title', 'body')
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(Note, NoteAdmin)