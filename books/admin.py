from django.contrib import admin

from .models import BxBooks
from .models import BxUsers
from .models import BxBookRatings

admin.site.register(BxBooks)
admin.site.register(BxBookRatings)
admin.site.register(BxUsers)