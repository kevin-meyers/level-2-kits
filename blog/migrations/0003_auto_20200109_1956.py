# Generated by Django 3.0.1 on 2020-01-09 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_summary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='modified',
            new_name='modified_at',
        ),
        migrations.AddField(
            model_name='blog',
            name='thumbnail_url',
            field=models.URLField(default='https://thumbs.dreamstime.com/z/tv-test-image-card-rainbow-multi-color-bars-geometric-signals-retro-hardware-s-minimal-pop-art-print-suitable-89603635.jpg'),
        ),
    ]