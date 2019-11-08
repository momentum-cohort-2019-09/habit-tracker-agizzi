from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Goal, History
# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Goal)
admin.site.register(History)