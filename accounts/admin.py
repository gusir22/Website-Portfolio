# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = [
        "email",
        "username",
        "age",
        "is_staff",
    ]
    # fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age",)}),)  # Add custom fieldset after default ones
    fieldsets = (
        ("Account Information", {"fields": ("username", "password",)}),
        ("Personal Information", {"fields": ("first_name", "last_name", "age",)}),
        ("Contact Information", {"fields": ("email",)}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )
    # add_fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age",)}),)
    add_fieldsets = fieldsets  # Exact same as fieldset


admin.site.register(CustomUser, CustomUserAdmin)
