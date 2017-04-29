# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class BxBookRatings(models.Model):
    user_id = models.IntegerField(db_column='User-ID')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    isbn = models.CharField(db_column='ISBN', max_length=13)  # Field name made lowercase.
    book_rating = models.IntegerField(db_column='Book-Rating')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'BX-Book-Ratings'
        unique_together = (('user_id', 'isbn'),)


class BxBooks(models.Model):
    isbn = models.CharField(db_column='ISBN', primary_key=True, max_length=13)  # Field name made lowercase.
    book_title = models.CharField(db_column='Book-Title', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    book_author = models.CharField(db_column='Book-Author', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    year_of_publication = models.IntegerField(db_column='Year-Of-Publication', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    publisher = models.CharField(db_column='Publisher', max_length=255, blank=True, null=True)  # Field name made lowercase.
    image_url_s = models.CharField(db_column='Image-URL-S', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    image_url_m = models.CharField(db_column='Image-URL-M', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    image_url_l = models.CharField(db_column='Image-URL-L', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'BX-Books'


class BxUsers(models.Model):
    user_id = models.IntegerField(db_column='User-ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location = models.CharField(db_column='Location', max_length=250, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BX-Users'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
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
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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
