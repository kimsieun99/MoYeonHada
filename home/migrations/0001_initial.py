# Generated by Django 4.2.3 on 2023-08-15 10:04

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(help_text='주로 사용하는 이메일주소를 입력해주세요 ex) example@example.com', max_length=255, unique=True)),
                ('username', models.CharField(help_text='사용하실 아이디를 입력해주세요', max_length=200, unique=True)),
                ('nickname', models.CharField(help_text='사용하실 별명을 입력해주세요', max_length=200)),
                ('phone_number', models.CharField(help_text='핸드폰 주소를 입력해주세요', max_length=200)),
                ('profile_image', models.ImageField(blank=True, upload_to='images/')),
                ('status', models.CharField(choices=[('teacher', '선생님입니다'), ('student', '배우미입니다')], default='student', max_length=20)),
                ('region_big', models.CharField(choices=[('서울', '서울'), ('경기도', '경기도'), ('강원도', '강원도'), ('충청도', '충청도'), ('전라도', '전라도'), ('경상도', '경상도'), ('인천', '인천'), ('대전', '대전'), ('광주', '광주'), ('대구', '대구'), ('울산', '울산'), ('부산', '부산'), ('제주', '제주')], default='student', max_length=20)),
                ('region_small', models.CharField(blank=True, default='', help_text='시 / 구 까지 작성해주세요', max_length=20, null=True)),
                ('region', models.CharField(default='서울시', max_length=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
