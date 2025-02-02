from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from okp.core.fields import OkpImageField
from okp.core.utils import get_slug
from okp.core.validators import okp_image_size_validator

User = get_user_model()


class OkpBlog(models.Model):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=200
    )
    slug = models.SlugField(
        verbose_name=_("Slug"),
        max_length=255,
        blank=True,
    )
    is_slug_auto = models.BooleanField(
        verbose_name=_("Auto-Generate Slug"),
        default=True,
    )
    description = models.TextField(
        verbose_name=_("Description"),
        blank=True,
    )
    total_posts = models.IntegerField(
        verbose_name=_("Total Posts"),
        default=0,
    )
    total_comments = models.IntegerField(
        verbose_name=_("Total Comments"),
        default=0,
    )
    is_active = models.BooleanField(
        verbose_name=_("Is Active"),
        default=True,
    )
    created_at = models.DateTimeField(
        verbose_name=_("Created At"),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated At"),
        auto_now=True,
    )

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")
        ordering = ["-updated_at", "-created_at"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.is_slug_auto:
            self.slug = get_slug(self.name, self, OkpBlog)
        super().save(*args, **kwargs)


class OkpBlogCategory(models.Model):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=200,
    )
    slug = models.SlugField(
        verbose_name=_("Slug"),
        max_length=255,
        blank=True,
    )
    is_slug_auto = models.BooleanField(
        verbose_name=_("Auto-Generate Slug"),
        default=True,
    )
    description = models.TextField(
        verbose_name=_("Description"),
        blank=True,
    )

    class Meta:
        verbose_name = _("Blog Category")
        verbose_name_plural = _("Blog Categories")
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.is_slug_auto:
            self.slug = get_slug(self.name, self, OkpBlogCategory)
        super().save(*args, **kwargs)


class OkpBlogTag(models.Model):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=200,
    )
    slug = models.SlugField(
        verbose_name=_("Slug"),
        max_length=255,
        blank=True,
    )
    is_slug_auto = models.BooleanField(
        verbose_name=_("Auto-Generate Slug"),
        default=True,
    )

    class Meta:
        verbose_name = _("Blog Tag")
        verbose_name_plural = _("Blog Tags")
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.is_slug_auto:
            self.slug = get_slug(self.name, self, OkpBlogTag)
        super().save(*args, **kwargs)


class OkpBlogPost(models.Model):
    blog = models.ForeignKey(
        OkpBlog,
        verbose_name=_("Blog"),
        on_delete=models.CASCADE,
        related_name="posts",
    )
    author = models.ForeignKey(
        User,
        verbose_name=_("Author"),
        on_delete=models.SET_NULL,
        related_name="blog_posts",
        null=True,
    )
    category = models.ForeignKey(
        OkpBlogCategory,
        verbose_name=_("Category"),
        on_delete=models.SET_NULL,
        related_name="posts",
        blank=True,
        null=True,
    )
    tags = models.ManyToManyField(
        OkpBlogTag,
        verbose_name=_("Tags"),
        related_name="posts",
        blank=True,
    )
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=200,
        blank=False,
        null=False,
    )
    slug = models.SlugField(
        verbose_name=_("Slug"),
        max_length=255,
        blank=True,
    )
    is_slug_auto = models.BooleanField(
        verbose_name=_("Auto-Generate Slug"),
        default=True,
    )
    cover = OkpImageField(
        verbose_name=_("Cover"),
        upload_to="blogs/covers",
        max_width=1024,
        max_height=256,
        blank=True,
        null=True,
        validators=[
            okp_image_size_validator,
            FileExtensionValidator(
                allowed_extensions=["jpg", "jpeg", "png", "webp"]
            ),
        ],
    )
    content = models.TextField(
        verbose_name=_("Content"),
        blank=True,
    )
    total_comments = models.IntegerField(
        verbose_name=_("Total Comments"),
        default=0,
    )
    is_commentable = models.BooleanField(
        verbose_name=_("Is Commentable"),
        default=True,
        help_text=_("Enable comments for this post."),
    )
    is_comment_moderated = models.BooleanField(
        verbose_name=_("Is Comment Moderated"),
        default=True,
        help_text=_("Comments must be approved before being visible."),
    )
    is_published = models.BooleanField(
        verbose_name=_("Is Published"),
        default=False,
    )
    published_at = models.DateTimeField(
        verbose_name=_("Published At"),
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name=_("Created At"),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated At"),
        auto_now=True,
    )

    class Meta:
        verbose_name = _("Blog Post")
        verbose_name_plural = _("Blog Posts")
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_slug_auto:
            self.slug = get_slug(self.title, self, OkpBlogPost)
        if self.is_published and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)


class OkpBlogPostComment(models.Model):
    post = models.ForeignKey(
        OkpBlogPost,
        verbose_name=_("Post"),
        on_delete=models.CASCADE,
        related_name="comments",
    )
    author = models.ForeignKey(
        User,
        verbose_name=_("Author"),
        on_delete=models.SET_NULL,
        related_name="blog_comments",
        null=True,
    )
    content = models.TextField(
        verbose_name=_("Content"),
        blank=True,
    )
    is_visible = models.BooleanField(
        verbose_name=_("Is Visible"),
        default=False,
    )
    created_at = models.DateTimeField(
        verbose_name=_("Created At"),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated At"),
        auto_now=True,
    )

    class Meta:
        verbose_name = _("Blog Comment")
        verbose_name_plural = _("Blog Comments")
        ordering = ["-created_at"]

    def __str__(self):
        return self.content
