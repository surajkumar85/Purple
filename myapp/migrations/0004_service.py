# Generated by Django 3.2.4 on 2021-06-02 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_banner_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img')),
                ('btn_text', models.CharField(max_length=50)),
                ('card_text', models.CharField(max_length=150)),
            ],
        ),
    ]