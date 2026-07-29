from django.shortcuts import render, redirect
from .models import Campaign, Donation


# -----------------------------------
#   DONATE PAGE
# -----------------------------------
def donate(request):
    return render(request, "donation/donate_now.html")


# -----------------------------------
#   DONATION FORM SUBMIT (POST)
# -----------------------------------
def donation_success(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        donation_type = request.POST.get("donation_type")
        payment = request.POST.get("payment")
        amount = request.POST.get("amount")

        # Save donation in database
        Donation.objects.create(
            name=name,
            email=email,
            phone=phone,
            donation_type=donation_type,
            payment=payment,
            amount=amount
        )

        # Return success page with name
        return render(request, "donation/donation_success.html", {"name": name})

    # If user opens success URL without submitting form
    return redirect("donate")


# -----------------------------------
#   CAMPAIGN LIST PAGE
# -----------------------------------
def campaign_list(request):
    campaigns = Campaign.objects.all()
    return render(request, "donation/campaign_list.html", {"campaigns": campaigns})


# -----------------------------------
#   OPTIONAL — MAIN CAMPAIGNS PAGE
# -----------------------------------
def campaigns(request):
    data = Campaign.objects.all()
    return render(request, "donation/campaign_list.html", {"campaigns": data})
