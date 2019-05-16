from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe
from .forms import *
import json
from campaign.models import Campaign

@login_required
def index(request):
    campaigns = Campaign.objects.all()
    return render(request, 'campaign/index.html', {
        'campaigns': campaigns
    })

@login_required
def add(request):
    form = CampaignForm()
    return render(request, 'campaign/add.html',{
        'form': form
    })
