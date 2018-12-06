from django.contrib import admin
from .models import user, selfPost, twitterPost, instaPost
# Register your models here.
admin.site.register(user)
admin.site.register(selfPost)
admin.site.register(twitterPost)
admin.site.register(instaPost)