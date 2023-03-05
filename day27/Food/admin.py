from django.contrib import admin
from .models import Restaurant, Menu, Comment, Category
# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Category)


@admin.register(Comment)  
class CommentAdmin(admin.ModelAdmin):  
    list_display = ('name', 'email', 'post', 'created', 'active')  
    list_filter = ('active', 'created', 'updated')  
    search_fields = ('name', 'email', 'body')
