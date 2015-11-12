# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, max_length=80)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(null=True, blank=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(unique=True, max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
            ],
            options={
                'db_table': 'Comments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cpu',
            fields=[
                ('frequency', models.CharField(null=True, blank=True, max_length=64, db_column='Frequency')),
                ('brand', models.CharField(null=True, blank=True, max_length=32, db_column='Brand')),
                ('cmodel', models.CharField(primary_key=True, max_length=32, db_column='CModel', serialize=False)),
            ],
            options={
                'db_table': 'CPU',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customerservice',
            fields=[
                ('location', models.CharField(primary_key=True, max_length=255, db_column='Location', serialize=False)),
                ('brand', models.CharField(null=True, blank=True, max_length=32, db_column='Brand')),
            ],
            options={
                'db_table': 'CustomerService',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(null=True, blank=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(primary_key=True, max_length=40, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Graphicsprocessor',
            fields=[
                ('gmodel', models.CharField(primary_key=True, max_length=32, db_column='GModel', serialize=False)),
                ('brand', models.CharField(null=True, blank=True, max_length=32, db_column='Brand')),
                ('ramsize', models.CharField(null=True, blank=True, max_length=16, db_column='RamSize')),
            ],
            options={
                'db_table': 'GraphicsProcessor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Harddrive',
            fields=[
                ('hmodel', models.CharField(primary_key=True, max_length=32, db_column='HModel', serialize=False)),
                ('capacity', models.CharField(null=True, blank=True, max_length=32, db_column='Capacity')),
                ('interface', models.CharField(null=True, blank=True, max_length=32, db_column='Interface')),
            ],
            options={
                'db_table': 'HardDrive',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NewsletterSignup',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('email', models.CharField(max_length=254)),
                ('full_name', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField()),
                ('updated', models.DateTimeField()),
            ],
            options={
                'db_table': 'newsletter_signup',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('price', models.IntegerField(null=True, blank=True, db_column='Price')),
                ('quantity', models.IntegerField(null=True, blank=True, db_column='Quantity')),
            ],
            options={
                'db_table': 'Sell',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Warrant',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('wfrom', models.DateField(null=True, blank=True, db_column='WFrom')),
                ('until', models.DateField(null=True, blank=True, db_column='Until')),
            ],
            options={
                'db_table': 'Warrant',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('url', models.CharField(primary_key=True, max_length=255, db_column='URL', serialize=False)),
                ('popuarity', models.TextField(null=True, blank=True, db_column='Popuarity')),
                ('shipment', models.CharField(null=True, blank=True, max_length=32, db_column='Shipment')),
            ],
            options={
                'db_table': 'Website',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('lmodel', models.CharField(primary_key=True, max_length=32, db_column='LModel', serialize=False)),
                ('type', models.CharField(null=True, blank=True, max_length=32, db_column='Type')),
                ('weight', models.IntegerField(null=True, blank=True, db_column='Weight')),
                ('resolution', models.CharField(null=True, blank=True, max_length=16, db_column='Resolution')),
            ],
            options={
                'db_table': 'Laptop',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('rating', models.IntegerField(null=True, blank=True, db_column='Rating')),
            ],
            options={
                'db_table': 'Rate',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('rid', models.IntegerField(primary_key=True, db_column='RID', serialize=False)),
                ('rating', models.IntegerField(null=True, blank=True, db_column='Rating')),
                ('description', models.TextField(null=True, blank=True, db_column='Description')),
                ('usefulness', models.IntegerField(null=True, blank=True, db_column='Usefulness')),
            ],
            options={
                'db_table': 'Review',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('full_name', models.CharField(default='', max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('name', models.CharField(null=True, blank=True, max_length=20)),
                ('uid', models.IntegerField(primary_key=True, db_column='UID', serialize=False)),
                ('age', models.IntegerField(null=True, blank=True, db_column='Age')),
                ('gender', models.CharField(null=True, blank=True, max_length=5, db_column='Gender')),
                ('job', models.CharField(null=True, blank=True, max_length=20, db_column='Job')),
                ('favorite', models.CharField(null=True, blank=True, max_length=100)),
            ],
            options={
                'db_table': 'Users',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Include',
            fields=[
                ('lmodel', models.ForeignKey(db_column='LModel', to='laptop.Laptop', primary_key=True, serialize=False)),
                ('cmodel', models.CharField(null=True, blank=True, max_length=32, db_column='CModel')),
                ('gmodel', models.CharField(null=True, blank=True, max_length=32, db_column='GModel')),
                ('hmodel', models.CharField(null=True, blank=True, max_length=32, db_column='HModel')),
            ],
            options={
                'db_table': 'Include',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='rate',
            name='uid',
            field=models.ForeignKey(to='laptop.Users', db_column='UID'),
        ),
        migrations.AddField(
            model_name='rate',
            name='url',
            field=models.ForeignKey(to='laptop.Website', db_column='URL'),
        ),
        migrations.AlterUniqueTogether(
            name='rate',
            unique_together=set([('url', 'uid')]),
        ),
    ]
