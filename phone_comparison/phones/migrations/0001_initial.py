# Generated by Django 3.0.6 on 2020-06-18 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('os', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='AndroidPhone',
            fields=[
                ('phone_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='phones.Phone')),
                ('android_version', models.CharField(max_length=10)),
            ],
            bases=('phones.phone',),
        ),
        migrations.CreateModel(
            name='ApplePhone',
            fields=[
                ('phone_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='phones.Phone')),
                ('ios_version', models.CharField(max_length=10)),
            ],
            bases=('phones.phone',),
        ),
        migrations.CreateModel(
            name='HuaweiPhone',
            fields=[
                ('phone_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='phones.Phone')),
                ('app_galery_version', models.CharField(max_length=10)),
            ],
            bases=('phones.phone',),
        ),
    ]
