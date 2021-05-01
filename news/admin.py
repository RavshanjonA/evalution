from django.contrib import admin

from .models import (Category, Region, Article, Attachment, Message, Employee)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description')


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'published_at', 'review', 'slug')
    search_fields = ['title']


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('article', 'order', 'image')
    autocomplete_fields = ['article']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone_number', 'theme', 'created_at')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position')
