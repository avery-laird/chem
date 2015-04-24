from django.contrib import admin
from mezzanine.conf import settings
from mezzanine.core.admin import DisplayableAdmin, DisplayableAdminForm, TabularDynamicInlineAdmin
from mezzanine.pages.models import Page, RichTextPage, Link
from mezzanine.pages.admin import PageAdmin
from mezzanine.utils.urls import admin_url

from copy import deepcopy
from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.models import BlogPost

from theme.models import HomePage, Slide, ExtendedBlog

blog_fieldsets = deepcopy(BlogPostAdmin.fieldsets)
blog_fieldsets[0][1]["fields"].insert(-2, "use_dark_background")

class MyBlogPostAdmin(BlogPostAdmin):
    fieldsets = blog_fieldsets

class SlideInline(TabularDynamicInlineAdmin):
    model = Slide

class HomePageAdmin(PageAdmin):
    inlines = (SlideInline,)

class ExtendedBlogAdmin(PageAdmin):
    pass

admin.site.register(ExtendedBlog, ExtendedBlogAdmin)
admin.site.register(HomePage, HomePageAdmin)
admin.site.unregister(BlogPost)
admin.site.register(BlogPost, MyBlogPostAdmin)
# Register your models here.
