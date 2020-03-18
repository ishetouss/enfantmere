from django.contrib import admin
from .models import Blog, Comment, SendMessage
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created']
    
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author','body']
    

class SendMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']

    

admin.site.register(Blog, BlogAdmin)
admin.site.register(SendMessage, SendMessageAdmin)
admin.site.register(Comment, CommentAdmin)