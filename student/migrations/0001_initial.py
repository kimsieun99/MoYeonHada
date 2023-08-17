# Generated by Django 4.2.3 on 2023-08-17 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('number', models.PositiveIntegerField()),
                ('content', models.TextField()),
                ('photo', models.ImageField(blank=True, upload_to='images/')),
                ('period1', models.DateField(default='', max_length=50)),
                ('period2', models.DateField(default='', max_length=50)),
                ('region', models.CharField(default='', max_length=50)),
                ('field', models.CharField(choices=[('휴대전화', '휴대전화'), ('인터넷', '인터넷'), ('키오스크', '키오스크'), ('생활편의', '생활편의'), ('기타', '기타')], default='', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Students', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='StudentComments', to='student.student')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='StudentComments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]