from django.contrib import admin
from blogging.models import Post, Category

class CategoryInLine(admin.TabularInline):
    model = Category.posts.through

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInLine,
    ]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
