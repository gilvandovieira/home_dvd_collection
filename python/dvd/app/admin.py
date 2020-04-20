from django.contrib import admin
from .models import Ator, Filme


# class AtorAdmin(admin.ModelAdmin):
#     list_display = ('nome',)


admin.site.register(Ator)
admin.site.register(Filme)
