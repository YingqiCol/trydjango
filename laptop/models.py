from __future__ import unicode_literals
from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.


from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    uid = models.IntegerField(db_column='UID', primary_key=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=5, blank=True, null=True)  # Field name made lowercase.
    job = models.CharField(db_column='Job', max_length=20, blank=True, null=True)  # Field name made lowercase.
    favorite = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Users'

    def __str__(self):
        return self.name


class Laptop(models.Model):
    lmodel = models.CharField(db_column='LModel', primary_key=True, max_length=32)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=32, blank=True, null=True)  # Field name made lowercase.
    weight = models.IntegerField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    resolution = models.CharField(db_column='Resolution', max_length=16, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Laptop'

    def __str__(self):
        return self.lmodel


class Cpu(models.Model):
    frequency = models.CharField(db_column='Frequency', max_length=64, blank=True, null=True)  # Field name made lowercase.
    brand = models.CharField(db_column='Brand', max_length=32, blank=True, null=True)  # Field name made lowercase.
    cmodel = models.CharField(db_column='CModel', primary_key=True, max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CPU'

    def __str__(self):
        return self.cmodel


class Comments(models.Model):
    lmodel = models.ForeignKey('Laptop', db_column='LModel')  # Field name made lowercase.
    rid = models.ForeignKey('Review', db_column='RID')  # Field name made lowercase.
    uid = models.ForeignKey('Users', db_column='UID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Comments'
        unique_together = (('lmodel', 'rid', 'uid'),)

    def __str__(self):
        return self.rid.description


class Website(models.Model):
    url = models.CharField(db_column='URL', primary_key=True, max_length=255)  # Field name made lowercase.
    popuarity = models.TextField(db_column='Popuarity', blank=True, null=True)  # Field name made lowercase.
    shipment = models.CharField(db_column='Shipment', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Website'

    def __str__(self):
        return self.url


class Customerservice(models.Model):
    location = models.CharField(db_column='Location', primary_key=True, max_length=255)  # Field name made lowercase.
    brand = models.CharField(db_column='Brand', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CustomerService'


class Graphicsprocessor(models.Model):
    gmodel = models.CharField(db_column='GModel', primary_key=True, max_length=32)  # Field name made lowercase.
    brand = models.CharField(db_column='Brand', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ramsize = models.CharField(db_column='RamSize', max_length=16, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GraphicsProcessor'

    def __str__(self):
        return  self.gmodel






class Harddrive(models.Model):
    hmodel = models.CharField(db_column='HModel', primary_key=True, max_length=32)  # Field name made lowercase.
    capacity = models.CharField(db_column='Capacity', max_length=32, blank=True, null=True)  # Field name made lowercase.
    interface = models.CharField(db_column='Interface', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HardDrive'

    def __str__(self):
        return self.hmodel


class Include(models.Model):
    lmodel = models.ForeignKey('Laptop', db_column='LModel', primary_key=True)  # Field name made lowercase.
    cmodel = models.CharField(db_column='CModel', max_length=32, blank=True, null=True)  # Field name made lowercase.
    gmodel = models.CharField(db_column='GModel', max_length=32, blank=True, null=True)  # Field name made lowercase.
    hmodel = models.CharField(db_column='HModel', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Include'

    def  __str__(self):
          return self.lmodel.lmodel




class Rate(models.Model):
    uid = models.ForeignKey('Users', db_column='UID')  # Field name made lowercase.
    url = models.ForeignKey('Website', db_column='URL')  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Rate'
        unique_together = (('url', 'uid'),)


class Review(models.Model):
    rid = models.IntegerField(db_column='RID', primary_key=True)  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    usefulness = models.IntegerField(db_column='Usefulness', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Review'


class Sell(models.Model):
    lmodel = models.ForeignKey(Laptop, db_column='LModel')  # Field name made lowercase.
    url = models.ForeignKey('Website', db_column='URL')  # Field name made lowercase.
    price = models.IntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sell'
        unique_together = (('url', 'lmodel'),)





class Warrant(models.Model):
    lmodel = models.ForeignKey(Laptop, db_column='LModel')  # Field name made lowercase.
    location = models.ForeignKey(Customerservice, db_column='Location')  # Field name made lowercase.
    wfrom = models.DateField(db_column='WFrom', blank=True, null=True)  # Field name made lowercase.
    until = models.DateField(db_column='Until', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Warrant'
        unique_together = (('lmodel', 'location'),)





class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.ForeignKey(AuthGroup)
    permission_id = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.ForeignKey(AuthUser)
    group_id = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.ForeignKey(AuthUser)
    permission_id = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


# class BooksAuthor(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.CharField(max_length=254)
#
#     class Meta:
#         managed = False
#         db_table = 'books_author'
#
#
# class BooksBook(models.Model):
#     title = models.CharField(max_length=100)
#     publication_date = models.DateField()
#     publisher = models.ForeignKey('BooksPublisher')
#
#     class Meta:
#         managed = False
#         db_table = 'books_book'
#
#
# class BooksBookAuthors(models.Model):
#     book = models.ForeignKey(BooksBook)
#     author = models.ForeignKey(BooksAuthor)
#
#     class Meta:
#         managed = False
#         db_table = 'books_book_authors'
#         unique_together = (('book_id', 'author_id'),)
#
#
# class BooksPublisher(models.Model):
#     name = models.CharField(max_length=30)
#     address = models.CharField(max_length=50)
#     city = models.CharField(max_length=60)
#     state = models.CharField(max_length=30)
#     country = models.CharField(max_length=50)
#     website = models.CharField(max_length=200)
#
#     class Meta:
#         managed = False
#         db_table = 'books_publisher'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class NewsletterSignup(models.Model):
    email = models.CharField(max_length=254)
    full_name = models.CharField(max_length=120)
    timestamp = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'newsletter_signup'

class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120, default='', null=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return self.email