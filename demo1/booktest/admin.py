from django.contrib import admin

# Register your models here.
from.models import BookInfo,HeroInfo

class BookInfoAdmin(admin.ModelAdmin):
    list_display=("title")

admin.site.register(BookInfo)
admin.site.register(HeroInfo)