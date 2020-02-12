from django.contrib import admin
from .models import Category, ChildCategory, Tag, Blog  # BlogTag

# Register your models here.
admin.site.register(Category)
admin.site.register(ChildCategory)
admin.site.register(Tag)
admin.site.register(Blog)
# admin.site.register(BlogTag)
