from django.contrib import admin

from okp.contrib.blog.models import (
    OkpBlog,
    OkpBlogCategory,
    OkpBlogTag,
    OkpBlogPost,
    OkpBlogPostComment,
)


@admin.register(OkpBlog)
class OkpBlogAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_active")
    search_fields = ("name", "slug")
    list_filter = ("is_active",)


@admin.register(OkpBlogCategory)
class OkpBlogCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", "slug")


@admin.register(OkpBlogTag)
class OkpBlogTagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name", "slug")


@admin.register(OkpBlogPost)
class OkpBlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "is_published")
    search_fields = ("title", "slug")
    list_filter = ("is_published",)


@admin.register(OkpBlogPostComment)
class OkpBlogPostCommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "is_visible")
    search_fields = ("post__title", "author__username")
    list_filter = ("is_visible",)
