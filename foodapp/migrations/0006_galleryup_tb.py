# Generated by Django 4.1.3 on 2022-12-14 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0005_reservation_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='galleryup_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=255)),
                ('gimg', models.ImageField(upload_to='product/')),
            ],
        ),
    ]
