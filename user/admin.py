from django.contrib import admin

from .models import Wallet, User

# Register your models here.

admin.site.register([Wallet, User])
