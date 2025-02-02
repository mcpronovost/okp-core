from django.db import transaction
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from okp.contrib.blog.models import OkpBlog, OkpBlogPost, OkpBlogPostComment


@receiver([post_save, post_delete], sender=OkpBlogPost)
def update_blog_total_posts(_sender, instance, **kwargs):
    """
    Update the total_posts count of the related blog
    using database aggregation
    """
    blog = instance.blog

    total_posts = blog.posts.count()

    OkpBlog.objects.filter(id=blog.id).update(
        total_posts=total_posts
    )


@receiver([post_save, post_delete], sender=OkpBlogPostComment)
def update_blog_total_comments(_sender, instance, **kwargs):
    """
    Update the total_comments count of the related blog
    and post using database aggregation in a single transaction
    """
    post = instance.post

    with transaction.atomic():
        total_comments = post.comments.count()

        OkpBlog.objects.filter(id=post.blog.id).update(
            total_comments=total_comments
        )
        OkpBlogPost.objects.filter(id=post.id).update(
            total_comments=total_comments
        )
