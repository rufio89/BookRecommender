from __future__ import unicode_literals

from django.db import models

class BxBookRatings(models.Model):
    user_id = models.IntegerField(db_column='User-ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
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