from django.contrib import admin
from blog.models import Post, Category
from django_summernote.admin import SummernoteModelAdmin

#@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = 'Not set'
    #fields = ('title',)
    #exclude = ('content',)
    list_display = ('title','author','counted_views','status','published_date','created_date')
    list_filter = ('status','author')
    #ordering = ['-created_date']
    search_fields = ['title','content']
    summernote_fields = ('content',)
    
admin.site.register(Post,PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']
    list_filter = ('name',)
    empty_value_display = 'Uncategorized'
     
admin.site.register(Category,CategoryAdmin)