# Generated by Django 4.2.5 on 2023-11-26 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='dp/menu_images/%Y/%m/%d')),
                ('price', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=400)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
                ('is_cafe', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='dp/store_images/%Y/%m/%d')),
                ('discount', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=300, unique=True)),
                ('password', models.CharField(max_length=400)),
                ('points', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='후기')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dp.store')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_points', models.PositiveIntegerField(default=0)),
                ('points_used', models.PositiveIntegerField(default=0)),
                ('total_amount', models.PositiveIntegerField(default=0)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dp.menu')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dp.store')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dp.user')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dp.store'),
        ),
    ]
