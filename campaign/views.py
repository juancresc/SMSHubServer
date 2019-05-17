from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe
from .forms import *
import json
from campaign.models import Campaign
from django.contrib import messages

@login_required
def index(request):
    campaigns = Campaign.objects.all()
    return render(request, 'campaign/index.html', {
        'campaigns': campaigns
    })

@login_required
def add(request):
    errors = False
    if request.method == 'POST':
        form = CampaignForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Campaign saved')
            return index(request)
        else:
            errors = form.errors
    form = CampaignForm()
    return render(request, 'campaign/add.html',{
        'form': form,
        'errors': errors
    })
