
"""
from django.contrib import admin
from blogging.models import Post, Category
admin.site.register(Post)
admin.site.register(Category)
"""
from blogging.models import Post, Category, AdminModel
from django.contrib import admin


class ModelAdminClass(admin.TabularInline):
    model = AdminModel
    extra = 1


class AdminPostClass(admin.ModelAdmin):
    inlines = (ModelAdminClass,)


class AdminCategoryClass(admin.ModelAdmin):
    exclude = ('posts',)


admin.site.register(Post, AdminPostClass)
admin.site.register(Category, AdminCategoryClass)



