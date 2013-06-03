from django.contrib import admin
from blog.models import Post, Category

class PostAdmin(admin.ModelAdmin):
    #exclude = ['posted']
    prepopulated_fields = {'readeble_url': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'readeble_url': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)