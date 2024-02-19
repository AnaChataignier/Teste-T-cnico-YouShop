from django.contrib import admin
from .models import Account, Tree, PlantedTree, User
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(admin.ModelAdmin):
    list_display = ("name", "created", "active")
    list_editable = ("active",)


class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "email")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
        (
            "Account Info",
            {"fields": ("accounts",)},
        ),  # Field to associate user with an account
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "accounts"),
            },
        ),
    )


class PlantedTreeInline(admin.TabularInline):
    model = PlantedTree
    extra = 0
    readonly_fields = (
        "planted_at",
        "user",
        "tree",
    )
    can_delete = False
    max_num = 0


class TreeAdmin(admin.ModelAdmin):
    list_display = ("name", "scientific_name")
    inlines = [PlantedTreeInline]


admin.site.register(Tree, TreeAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Account, AccountAdmin)
