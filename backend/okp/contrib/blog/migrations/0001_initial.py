# Generated by Django 5.1.5 on 2025-02-02 01:23

import django.core.validators
import django.db.models.deletion
import okp.core.fields
import okp.core.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OkpBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('slug', models.SlugField(blank=True, max_length=255, verbose_name='Slug')),
                ('is_slug_auto', models.BooleanField(default=True, verbose_name='Auto-Generate Slug')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('total_posts', models.IntegerField(default=0, verbose_name='Total Posts')),
                ('total_comments', models.IntegerField(default=0, verbose_name='Total Comments')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
                'ordering': ['-updated_at', '-created_at'],
            },
        ),
        migrations.CreateModel(
            name='OkpBlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('slug', models.SlugField(blank=True, max_length=255, verbose_name='Slug')),
                ('is_slug_auto', models.BooleanField(default=True, verbose_name='Auto-Generate Slug')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Blog Category',
                'verbose_name_plural': 'Blog Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='OkpBlogTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('slug', models.SlugField(blank=True, max_length=255, verbose_name='Slug')),
                ('is_slug_auto', models.BooleanField(default=True, verbose_name='Auto-Generate Slug')),
            ],
            options={
                'verbose_name': 'Blog Tag',
                'verbose_name_plural': 'Blog Tags',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='OkpBlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('slug', models.SlugField(blank=True, max_length=255, verbose_name='Slug')),
                ('is_slug_auto', models.BooleanField(default=True, verbose_name='Auto-Generate Slug')),
                ('cover', okp.core.fields.OkpImageField(blank=True, null=True, upload_to='blogs/covers', validators=[okp.core.validators.okp_image_size_validator, django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp'])], verbose_name='Cover')),
                ('content', models.TextField(blank=True, verbose_name='Content')),
                ('total_comments', models.IntegerField(default=0, verbose_name='Total Comments')),
                ('is_commentable', models.BooleanField(default=True, help_text='Enable comments for this post.', verbose_name='Is Commentable')),
                ('is_comment_moderated', models.BooleanField(default=True, help_text='Comments must be approved before being visible.', verbose_name='Is Comment Moderated')),
                ('is_published', models.BooleanField(default=False, verbose_name='Is Published')),
                ('published_at', models.DateTimeField(blank=True, null=True, verbose_name='Published At')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blog_posts', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='okp_blog.okpblog', verbose_name='Blog')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to='okp_blog.okpblogcategory', verbose_name='Category')),
                ('tags', models.ManyToManyField(blank=True, related_name='posts', to='okp_blog.okpblogtag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Blog Post',
                'verbose_name_plural': 'Blog Posts',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='OkpBlogPostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, verbose_name='Content')),
                ('is_visible', models.BooleanField(default=False, verbose_name='Is Visible')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blog_comments', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='okp_blog.okpblogpost', verbose_name='Post')),
            ],
            options={
                'verbose_name': 'Blog Comment',
                'verbose_name_plural': 'Blog Comments',
                'ordering': ['-created_at'],
            },
        ),
    ]
