# Generated by Django 2.2.6 on 2019-10-30 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_restaurant_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='flavours',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='score',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='tags',
            field=models.ManyToManyField(related_name='restaurants', to='api.Tag'),
        ),
    ]
