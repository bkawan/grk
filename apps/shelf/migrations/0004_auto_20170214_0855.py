# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 08:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0003_auto_20170214_0808'),
    ]

    operations = [
        migrations.CreateModel(
            name='Identifiers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('code', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='TableOfContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
        ),
        migrations.RenameField(
            model_name='book',
            old_name='isbn',
            new_name='isbn_10',
        ),
        migrations.AddField(
            model_name='book',
            name='isbn_13',
            field=models.PositiveIntegerField(default=1234, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='lccn',
            field=models.IntegerField(default=43),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='number_of_pages',
            field=models.IntegerField(default=46),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='oclc_number',
            field=models.IntegerField(default=435),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='pagination',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='physical_dimensions',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='published_date',
            field=models.DateField(default='2017-02-02'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='revision',
            field=models.IntegerField(default=43),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='weight',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='genre',
            field=models.ManyToManyField(blank=True, to='shelf.Genre'),
        ),
        migrations.AlterField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(blank=True, to='shelf.Tag'),
        ),
        migrations.AddField(
            model_name='tableofcontent',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='table_of_contents', to='shelf.Book'),
        ),
        migrations.AddField(
            model_name='identifiers',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='identifiers', to='shelf.Book'),
        ),
        migrations.AddField(
            model_name='book',
            name='publishers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shelf.Publisher'),
        ),
    ]
