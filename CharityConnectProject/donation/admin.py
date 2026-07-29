from django.contrib import admin
from .models import Campaign, Donation


# -----------------------------------
#   CAMPAIGN ADMIN
# -----------------------------------
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('title', 'goal_amount', 'raised_amount', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    search_fields = ('title',)
    ordering = ('start_date',)
    list_editable = ('goal_amount', 'raised_amount')


# Register Campaign
admin.site.register(Campaign, CampaignAdmin)


# -----------------------------------
#   DONATION ADMIN
# -----------------------------------
class DonationAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "amount", "donation_type", "payment", "created_at")
    list_filter = ("donation_type", "payment", "created_at")
    search_fields = ("name", "email", "phone")
    ordering = ("-created_at",)


# Register Donation
admin.site.register(Donation, DonationAdmin)
