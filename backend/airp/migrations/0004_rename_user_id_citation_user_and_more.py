# Generated by Django 4.2.11 on 2024-03-12 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airp', '0003_alter_author_created_at_alter_author_updated_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='citation',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='citereview',
            old_name='citation_id',
            new_name='citation',
        ),
        migrations.RenameField(
            model_name='citereview',
            old_name='reviewer_id',
            new_name='reviewer',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='author_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='citation_id',
            new_name='citation',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='reviewer_id',
            new_name='reviewer',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='sender_id',
            new_name='sender',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='source_id',
            new_name='source',
        ),
        migrations.RenameField(
            model_name='source',
            old_name='author_id',
            new_name='author',
        ),
    ]
