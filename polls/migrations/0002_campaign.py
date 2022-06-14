# Generated by Django 4.0.5 on 2022-06-10 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign_code', models.IntegerField(null=True)),
                ('name', models.CharField(db_index=True, max_length=150, unique=True)),
                ('AS400Promotion', models.IntegerField(default=9998)),
                ('days', models.CharField(default='1111111', max_length=7)),
                ('type', models.IntegerField(default=99)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_valid', models.BooleanField(default=False)),
                ('priority', models.PositiveSmallIntegerField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]