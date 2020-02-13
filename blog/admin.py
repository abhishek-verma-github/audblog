from django.contrib import admin
from .models import Category, ChildCategory, Tag, Blog  # BlogTag
from django.contrib.auth import get_user_model
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'category')
    list_filter = ('created_on', 'category')

    # fields = ('image_tag', 'title', 'content', 'status',
    #           'created_on', 'updated_on', 'category', 'tags', 'author')
    # readonly_fields = ('image_tag',)

    # to get the current logged in user in admin panel-------------------------------------------
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['queryset'] = get_user_model().objects.filter(
                username=request.user.username)
        return super(BlogAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return self.readonly_fields + ('author',)
        return self.readonly_fields

    def add_view(self, request, form_url="", extra_context=None):
        data = request.GET.copy()
        data['author'] = request.user
        request.GET = data
        return super(BlogAdmin, self).add_view(request, form_url="", extra_context=extra_context)
    # --------------------------------------------------------------------------------------------


admin.site.site_header = 'Audblog Admin Panel'
admin.site.register(Category)
admin.site.register(ChildCategory)
admin.site.register(Tag)
admin.site.register(Blog, BlogAdmin)
# admin.site.register(BlogTag)
