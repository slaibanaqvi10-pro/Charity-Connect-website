from django.db import models

# ----------------------
#   CAMPAIGN MODEL
# ----------------------
class Campaign(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100, null=True, blank=True)
    organizer = models.CharField(max_length=100, null=True, blank=True)
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    raised_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title


# ----------------------
#   DONATION MODEL
# ----------------------
class Donation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    donation_type = models.CharField(max_length=20)  # One-time / Monthly
    payment = models.CharField(max_length=50)        # Card / Paypal / Bank
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.amount}"
