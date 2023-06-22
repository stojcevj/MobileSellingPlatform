from django.contrib import admin

# Register your models here.
from MobileSellingApp.models import MobileListing, Profile


class MobileListingAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.listing_profile = request.user
        obj.save()


admin.site.register(MobileListing, MobileListingAdmin)


class ProfileAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.profile_user = request.user
        obj.save()


admin.site.register(Profile, ProfileAdmin)
