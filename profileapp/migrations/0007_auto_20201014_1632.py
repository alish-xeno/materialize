# Generated by Django 3.1.2 on 2020-10-14 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0006_customermessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=200)),
                ('icon', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='customermessage',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profileapp.gallery'),
        ),
        migrations.CreateModel(
            name='MessageSpecificationComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('comment', models.CharField(max_length=200)),
                ('message_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profileapp.customermessage')),
                ('specification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profileapp.specification')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='gallery',
            name='specifications',
            field=models.ManyToManyField(blank=True, to='profileapp.Specification'),
        ),
    ]
